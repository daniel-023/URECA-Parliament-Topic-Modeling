import pandas as pd
from wordcloud import WordCloud
from data_preprocessing import data_preparation, remove_stopwords, length_filter, speaker_count
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import os.path

data = data_preparation('Datasets/Parl_1.csv')

data['main_text'] = data['main_text'].apply(remove_stopwords)
# Set a relative path
folder_name = 'output'
current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
path = os.path.join(current_directory, folder_name)

# Overview
print("Original Data:")
rows, cols = data.shape
print(f"{rows} rows, {cols} columns")
print(f"Missing values in each column: \n{data.isnull().sum()}")
data['doc_length'] = data['main_text'].apply(lambda x: len(x.split()))

# Filtered Data
data = data.dropna()  # Remove rows with missing values
data = length_filter(data, 50)
new_rows, new_cols = data.shape
print("\nFiltered Data:")
print(f"{new_rows} rows, {new_cols} columns")
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
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(path, 'Top10_MP_frequency.png'))
