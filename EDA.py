import pandas as pd
from wordcloud import WordCloud
from data_preprocessing import load_data, preprocess_text, length_filter, speaker_count
import matplotlib.pyplot as plt
import os.path
from bertopic import BERTopic

data = load_data('Datasets/Parl_1.csv')

# Overview
print("Original Data:")
rows, cols = data.shape
print(f"{rows} rows, {cols} columns")
print(f"Missing values in each column: \n{data.isnull().sum()}")
data['doc_length'] = data['main_text'].apply(lambda x: len(x.split()))

# Filtered Data
data = data.dropna()  # Remove rows with missing values
data = length_filter(data, 200)
new_rows, new_cols = data.shape
print("\nFiltered Data:")
print(f"{new_rows} rows, {new_cols} columns")

# Preprocessing Text
speaker_names = list(speaker_count(data).keys())
data['main_text'] = data.apply('main_text').apply(lambda x: preprocess_text(x, speaker_names))
# Set a relative path
folder_name = 'output'
current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
path = os.path.join(current_directory, folder_name)

data.to_excel('Datasets\Excel_Dataset.xlsx', index=False)

# Text Data Analysis
plt.figure(figsize=(12, 8))
plt.hist(data['doc_length'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Document Lengths', fontsize=16)
plt.xlabel('Document Length (Number of Words)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(path, 'overall_doc_length.png'))

max_length = 2000
filtered_lengths = [length for length in data['doc_length'] if length < max_length]
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
all_words = ' '.join(data['main_text'])
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(all_words)
plt.figure(figsize=(12, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=5)
plt.savefig(os.path.join(path, 'text_wordcloud'))

print("\n")

# Speaker Analysis
speakers = speaker_count(data)
print(f"Total speakers:{len(speakers.keys())}")
speakers_df = pd.DataFrame(list(speakers.items()), columns=['MP_name', 'Frequency'])
top_speakers_df = speakers_df.sort_values(by='Frequency', ascending=False).head(10)

plt.figure(figsize=(15, 10))
plt.bar(top_speakers_df['MP_name'], top_speakers_df['Frequency'], color='Lavender')
plt.title('Top 10 MPs by Frequency in Documents', fontsize=16)
plt.xlabel('MP Name', ha = 'center', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12, ha='right', rotation=45)
plt.yticks(fontsize=12, ha='right')
plt.grid(True, alpha=0.8)
plt.tight_layout()
plt.savefig(os.path.join(path, 'Top10_MP_frequency.png'))




# Model Training
topic_model = BERTopic()
topics, probabilities = topic_model.fit_transform(data['main_text'])

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
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.tight_layout() # Adjust layout to not cut off labels
plt.savefig(os.path.join(path, 'topic_chart.png'))
