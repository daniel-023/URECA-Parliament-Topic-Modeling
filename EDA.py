import pandas as pd
from wordcloud import WordCloud
from data_preprocessing import load_data, preprocess_text, length_filter, speaker_count
import matplotlib.pyplot as plt
import os.path
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# from bertopic import BERTopic

df = pd.concat(map(pd.read_csv, ['Datasets/Parl_1.csv', 'Datasets/Parl_2.csv']), ignore_index=True)
print(df)

# Overview
print("Original Data:")
rows, cols = df.shape
print(f"{rows} rows, {cols} columns")
print(f"Missing values in each column: \n{df.isnull().sum()}")
df['doc_length'] = df['main_text'].apply(lambda x: len(x.split()))

# Filtered Data
df = df.dropna()  # Remove rows with missing values
df = length_filter(df, 200, 5000)
new_rows, new_cols = df.shape
print("\nFiltered Data:")
print(f"{new_rows} rows, {new_cols} columns")

# Preprocessing Text
df['main_text'] = df.apply('main_text').apply(lambda x: preprocess_text(x))
# Set a relative path
folder_name = 'output'
current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
path = os.path.join(current_directory, folder_name)

df.to_excel('Datasets/Excel_Dataset.xlsx', index=False)

# Text Data Analysis
plt.figure(figsize=(12, 8))
plt.hist(df['doc_length'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Document Lengths', fontsize=16)
plt.xlabel('Document Length (Number of Words)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(path, 'overall_doc_length.png'))

max_length = 2000
filtered_lengths = [length for length in df['doc_length'] if length < max_length]
plt.figure(figsize=(12, 8))
plt.hist(filtered_lengths, bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Document Lengths (Up to 2000 Words)', fontsize=16)
plt.xlabel('Document Length (Number of Words)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(path, 'filtered_doc_length.png'))

# Word Clouds
all_words = ' '.join(df['main_text'])
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(all_words)
plt.figure(figsize=(12, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=5)
plt.savefig(os.path.join(path, 'text_wordcloud'))

print("\n")

# Speaker Analysis
parl_1_speakers, parl_2_speakers = speaker_count(df, 1), speaker_count(df, 2)

parl_1_speakers_df = pd.DataFrame(list(parl_1_speakers.items()), columns=['MP_name', 'Frequency'])
top_parl1_speakers_df = parl_1_speakers_df.sort_values(by='Frequency', ascending=False).head(10)

parl_2_speakers_df = pd.DataFrame(list(parl_2_speakers.items()), columns=['MP_name', 'Frequency'])
top_parl2_speakers_df = parl_2_speakers_df.sort_values(by='Frequency', ascending=False).head(10)

plt.figure(figsize=(15, 10))
plt.bar(top_parl1_speakers_df['MP_name'], top_parl1_speakers_df['Frequency'], color='Lavender')
plt.title('Parl 1: Top 10 MPs by Frequency in Documents', fontsize=16)
plt.xlabel('MP Name', ha='center', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12, ha='right', rotation=45)
plt.yticks(fontsize=12, ha='right')
plt.grid(True, alpha=0.8)
plt.tight_layout()
plt.savefig(os.path.join(path, 'Parl1_Top10_MP_frequency.png'))

plt.figure(figsize=(15, 10))
plt.bar(top_parl2_speakers_df['MP_name'], top_parl2_speakers_df['Frequency'], color='Lavender')
plt.title('Parl 2: Top 10 MPs by Frequency in Documents', fontsize=16)
plt.xlabel('MP Name', ha='center', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12, ha='right', rotation=45)
plt.yticks(fontsize=12, ha='right')
plt.grid(True, alpha=0.8)
plt.tight_layout()
plt.savefig(os.path.join(path, 'Parl2_Top10_MP_frequency.png'))

# Model Training
vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")
topic_model = BERTopic(vectorizer_model=vectorizer_model, min_topic_size=10)
topics, probabilities = topic_model.fit_transform(df['main_text'])

# Topic Extraction
topic_info = topic_model.get_topic_info().set_index('Topic')[['Count', 'Name', 'Representation']]
topic_info.to_html('Output/topic_info_table.html')

# Topic Visualisation
fig = topic_model.visualize_topics()
fig.write_html("Output/topic_model_visualisation.html")

# Bar Chart
freq = topic_model.get_topic_info()

# Sorting the topics by 'Count' to get the most discussed topics
freq_sorted = freq.sort_values(by='Count', ascending=False)

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(freq_sorted['Name'], freq_sorted['Count'], color='skyblue')
plt.title('Volume of Discourse Across Different Topics')
plt.xlabel('Topics')
plt.ylabel('Number of Documents')
plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
plt.tight_layout()  # Adjust layout to not cut off labels
plt.savefig(os.path.join(path, 'topic_chart.png'))
