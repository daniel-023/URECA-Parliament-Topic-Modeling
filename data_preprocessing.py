import nltk
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def load_data(path):
    data = pd.read_csv(path)
    return data


def preprocess_text(text, speaker_names):
    text = re.sub(r'\r|\n', ' ', text)
    text = re.sub(r'(Head | Subhead) - \d+', '', text)
    text = re.sub(r'Column: \d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    lemmatizer = WordNetLemmatizer()
    custom_stopwords = ["mr speaker in the chair", "mr", "speaker", "sir", "parliament", "head", "subhead"]
# custom_stopwords.extend(speaker_names)
    all_stopwords = set(stopwords.words('english')).union(custom_stopwords)
    tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in all_stopwords]

    return ' '.join(tokens)

# remove outliers
# Create n-grams
# gradient clipping



def speaker_count(data):
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
    data = data[min_length <= data['doc_length'] <= max_length]
    return data
