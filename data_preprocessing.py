import nltk
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def load_data(path):
    data = pd.read_csv(path)
    return data


def preprocess_text(text):
    text = re.sub(r'\r|\n', ' ', text)
    text = re.sub(r'(Head | Subhead) - \d+', '', text)
    text = re.sub(r'Column: \d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    # lemmatizer = WordNetLemmatizer() custom_stopwords = ["mr speaker in the chair", "mr", "speaker", "sir",
    # "parliament", "head", "subhead", "singapore", "member", "government", "people", "minister", "would", "one",
    # "country", "public", "also", "amendment", "bill", "board", "development", "house", "year", "sum", "centre",
    # "beg", "time", "member", "provision", "clause", "committee", "move", "question", "may", "made",
    # "law"] custom_stopwords.extend(speaker_names) all_stopwords = set(stopwords.words('english')).union(
    # custom_stopwords)
    return text


# remove outliers
# Create n-grams
# gradient clipping

def speaker_count(data, parliament_no):
    data = data[data['parliament_no'] == parliament_no]
    speakers = data['MPs_speaking']
    speaker_dict = {}
    for row in speakers:
        for speaker in row.split(';'):
            if speaker != '':
                if speaker in speaker_dict:
                    speaker_dict[speaker] += 1
                else:
                    speaker_dict[speaker] = 1
    return speaker_dict


def length_filter(data, min_length, max_length):
    filtered_data = data[(data['doc_length'] >= min_length) & (data['doc_length'] <= max_length)]
    return filtered_data
