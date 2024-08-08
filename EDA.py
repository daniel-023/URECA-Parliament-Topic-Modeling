from data_preprocessing import *
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from utils import build_file_path


def data_info(df):
    rows, cols = df.shape
    print(f"{rows} rows, {cols} columns")
    print(df.info())


def doc_length_col(df):
    df['doc_length'] = df['main_text'].apply(lambda x: len(x.split()))
    return df['doc_length']


def parl_distribution(df):
    parliament_counts = df['parliament_no'].value_counts().reset_index()
    parliament_counts.columns = ['parliament', 'count']
    custom_colours = [
    'rgba(255, 182, 193, 1)',  # Pastel Pink
    'rgba(173, 216, 230, 1)',  # Pastel Blue
    'rgba(152, 251, 152, 1)'   # Pastel Green
    ]
    fig = px.bar(parliament_counts, x='parliament', y='count', labels={'parliament': 'Parliament', 'count': 'Count'}, color_discrete_sequence=[custom_colours[0]]
    , title='Distribution of Parliament Numbers')
    fig.update_xaxes(dtick=1)
    return fig


def sessions_over_time(df):
    df['sitting_date'] = pd.to_datetime(df['sitting_date'])

    # Group by year and month
    sessions_over_time = df.groupby(df['sitting_date'].dt.to_period('M')).size().reset_index(name='count')
    sessions_over_time['sitting_date'] = sessions_over_time['sitting_date'].astype(str)
    fig = px.line(sessions_over_time, x='sitting_date', y='count', title='Number of Sessions over Time', labels={'sitting_date': 'Date', 'count': 'Number of Sessions'})
    return fig


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


def word_cloud(df):
    text = ' '.join(df['title'])
    mask = np.array(Image.open('visualisations/singapore_flag_grey.png'))
    colours = ImageColorGenerator(mask)
    wordcloud = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='black', color_func=colours, stopwords=STOPWORDS, mask=mask, collocations=False).generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title("Word Cloud of Parliament Titles", fontsize=8, loc='left')
    return fig


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


