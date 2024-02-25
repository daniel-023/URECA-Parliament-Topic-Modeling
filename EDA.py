import pandas as pd
from wordcloud import WordCloud
from data_preprocessing import data_preparation
import matplotlib.pyplot as plt
import os.path

data = data_preparation('Datasets/Parl_1.csv')

# Set a relative path
folder_name = 'output'
current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
path = os.path.join(current_directory, folder_name)

# Overview
print(data.shape)
print(f"Missing values in each column: \n{data.isnull().sum()}")
print(f"Date range: {data['sitting_date'].min()} to {data['sitting_date'].max()}")

# Text Data Analysis
data['doc_length'] = data['main_text'].apply(lambda x: len(x.split()))
num_short_docs = data[data['doc_length'] < 50].shape[0]
print(f"No. of short documents: {num_short_docs}")

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
all_words = ' '.join(data['main_test)'].split())

# Speaker Analysis


# List of speakers, and count their occurences in the dataset.
