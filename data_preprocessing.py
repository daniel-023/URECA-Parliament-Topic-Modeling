import pandas as pd
import re


def combine_data(*files):
    path_list = []
    for file in files:
        path_list.append(f'Datasets/{file}')
    df = pd.concat(map(pd.read_csv, path_list), ignore_index=True)
    return df


def preprocess_text(text):
    text = re.sub(r'\r|\n', ' ', text)
    text = re.sub(r'(Head|Subhead) - \d+', '', text)
    text = re.sub(r'Column: \d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    custom_stopwords = {"mr", "speaker", "sir", "head"}
    words = [word for word in text.split() if word not in custom_stopwords]
    return ' '.join(words)


def length_filter(df, min_length):
    df = df.dropna()  # Remove rows with missing values
    filtered_data = df[(df['doc_length'] >= min_length)].reset_index(drop=True)
    return filtered_data
