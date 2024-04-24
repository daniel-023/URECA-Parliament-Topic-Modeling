from data_preprocessing import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from utils import build_file_path


# Overview
def data_info(df):
    rows, cols = df.shape
    print(f"{rows} rows, {cols} columns")
    print(df.info())


def doc_length_col(df):
    df['doc_length'] = df['main_text'].apply(lambda x: len(x.split()))
    return df['doc_length']


def parl_distribution(df, folder, filename):
    parliament_counts = df['parliament_no'].value_counts()
    labels = [
        f'Parliament 1 ({parliament_counts[1]})',
        f'Parliament 2 ({parliament_counts[2]})',
        f'Parliament 3 ({parliament_counts[3]})'
    ]
    y = [parliament_counts[1], parliament_counts[2], parliament_counts[3]]
    plt.figure(figsize=(8, 8))
    plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.savefig(build_file_path(folder, filename))


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
    data = df[df['parliament_no'] == parl_no]
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
    plt.bar(speaker_df( df, parl_no)['MP_name'], speaker_df(df, parl_no)['Frequency'], color='Lavender')
    plt.title(f'Parl {parl_no}: Top 10 MPs by Frequency in Documents', fontsize=16)
    plt.xlabel('MP Name', ha='center', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(fontsize=12, ha='right', rotation=45)
    plt.yticks(fontsize=12, ha='right')
    plt.grid(True, alpha=0.8)
    plt.tight_layout()
    plt.savefig(build_file_path(folder, filename))


