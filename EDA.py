from data_preprocessing import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os.path


# Overview
def describe_data(df):
    rows, cols = df.shape
    print(f"{rows} rows, {cols} columns")
    print(f"Missing values in each column: \n{df.isnull().sum()}")


def doc_length_col(df):
    df['doc_length'] = df['main_text'].apply(lambda x: len(x.split()))
    return df


# Set a relative path
def build_file_path(folder, filename):
    current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
    folder_path = os.path.join(current_directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, filename)
    return file_path


def write_excel(df, filename, folder):
    filepath = build_file_path(folder, filename)
    df.to_excel(filepath, index=False)


"""
create parliament distribution pie chart
"""


def length_distribution_hist(df, folder, filename):
    plt.figure(figsize=(12, 8))
    plt.hist(df['doc_length'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Document Lengths', fontsize=16)
    plt.xlabel('Document Length (Number of Words)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(build_file_path(folder, filename))


def word_cloud(df, folder, filename):
    all_words = ' '.join(df['main_text'])
    wordcloud = (WordCloud(width=800, height=800, background_color='white', min_font_size=10, stopwords=STOPWORDS)
                 .generate(all_words))
    plt.figure(figsize=(12, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=5)
    plt.savefig(build_file_path(folder, filename))


def speaker_count(df, parl_no):
    data = df[df['parliament_no'] == parliament_no]
    speakers = data['MPs_speaking']
    speaker_dict = {}
    for row in speakers:
        for speaker in row.split(';'):
            if speaker != '':
                speaker = speaker.strip()
                speaker_dict[speaker] = speaker_dict.get(speaker, 0) + 1
    return speaker_dict


def speaker_df(df, parl_no):
    parl_speakers = speaker_count(df, parl_no)
    top10 = (pd.DataFrame(list(parl_speakers.items()), columns=['MP_name', 'Frequency'])
             .sort_values(by='Frequency', ascending=False).head(10))
    return top10


def speaker_frequency_bar(df, parl_no, folder, filename):
    plt.figure(figsize=(15, 10))
    plt.bar(speaker_df(df, parl_no)['MP_name'], speaker_df(df, parl_no)['Frequency'], color='Lavender')
    plt.title(f'Parl {parl_no}: Top 10 MPs by Frequency in Documents', fontsize=16)
    plt.xlabel('MP Name', ha='center', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(fontsize=12, ha='right', rotation=45)
    plt.yticks(fontsize=12, ha='right')
    plt.grid(True, alpha=0.8)
    plt.tight_layout()
    plt.savefig(build_file_path(folder, filename))


