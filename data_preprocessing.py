import pandas as pd
import re


def data_preparation(path):
    data = pd.read_csv(path)  # loading data
    data['main_text'] = data['main_text'].str.replace('\r|\n', ' ', regex=True)  # Removing control characters
    data['main_text'] = data['main_text'].apply(lambda x: re.sub(r'(Head | Subhead) - \d+', '', x))
    data['main_text'] = data['main_text'].apply(lambda x: re.sub(r'Column: \d+', '', x))  # Removing column numbers
    data['main_text'] = data['main_text'].apply(lambda x: re.sub(r'\s+', ' ', x))  # Removing additional spaces

    data['main_text'] = data['main_text'].str.lower()  # Lowercase
    return data


def remove_stopwords(text):
    # Define your list of stopwords here
    stopwords = ["[mr speaker in the chair]", "mr", "speaker", "sir", "will"]

    # Combine the stopwords into a single regex pattern for efficiency
    stopwords_pattern = '|'.join(re.escape(word) for word in stopwords)

    # Use the compiled regex pattern to replace occurrences of the stopwords with an empty string
    cleaned_text = re.sub(stopwords_pattern, '', text, flags=re.IGNORECASE)

    return cleaned_text

def length_filter(data, min_length):
    data = data[data['doc_length'] >= min_length]
    return data
