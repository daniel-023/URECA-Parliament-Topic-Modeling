import pandas as pd
import re


def data_preparation(path):
    data = pd.read_csv(path)  # loading data
    data['main_text'] = data['main_text'].str.replace('\r|\n', ' ', regex=True)  # Removing control characters
    data['main_text'] = data['main_text'].apply(lambda x: re.sub(r'Column: \d+', '', x))  # Removing column numbers
    data['main_text'] = data['main_text'].apply(lambda x: re.sub(r'\s+', ' ', x))  # Removing additional spaces
    data['main_text'] = data['main_text'].str.lower()  # Lowercase

    return data
