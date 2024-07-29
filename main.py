from bertopic import BERTopic
from data_preprocessing import *
from EDA import *
from sentence_transformers import SentenceTransformer
from topic_modeling import *

# Loading and combining data
df = combine_data('Parl_1.csv', 'Parl_2.csv', 'Parl_3.csv')

df['main_text'] = df['main_text'].apply(preprocess_text)

df['doc_length'] = doc_length_col(df)

df = length_filter(df, 200)

length_distribution_hist(df, 'output', 'doc_length_distribution.png')

print(data_info(df))

word_cloud(df, 'output', 'wordcloud.png')

speaker_frequency_bar(df, 1, 'output', 'Parl1_Top10_Speakers')
speaker_frequency_bar(df, 2, 'output', 'Parl2_Top10_Speakers')
speaker_frequency_bar(df, 3, 'output', 'Parl3_Top10_Speakers')

parl_distribution(df, 'output', 'Parl_Distribution.png')

# To train a new topic model: 
# train_model(df['main_text'], 'Parliament_Topic_Model')
# exit()

# To load a model stored locally:
# loaded_model = load_model('Parliament_Topic_Model')


# Load the trained topic model from Hugging Face Hub
loaded_model = BERTopic.load("daniel-023/Parliament_Topic_Model")

topic_info = topic_extraction(loaded_model)

custom_topic_names = {
    0: 'Education',
    1: 'Land Development and Reclamation',
    2: 'Economy and Trade',
    3: 'Public Service',
    4: 'Law and Legislation',
    5: 'Citizenship and Immigration',
    6: 'Public Transport and Infrastructure',
    7: 'Property and Housing',
    8: 'Agriculture and Production',
    9: 'Diplomacy and Foreign Relations',
    10: 'Cultural Programmes and Media',
    11: 'Reproductive Rights and Family Planning',
    12: 'Retirement Fund',
    13: 'International Travel',
    14: 'Sports and National Events',
    15: 'Drug Control and Regulation',
    16: 'Public Helth',
    17: 'Fire and Emergency Services',
    18: 'Market and Hawker Licensing'
}

assign_topic_names(topic_info, custom_topic_names)

export_topic_info(topic_info)

intertopic_distance_map(loaded_model)

embeddings = load_embeddings('Parliament_Topic_Model')

visualise_documents(df['main_text'], loaded_model, embeddings=embeddings)

visualize_top_topics(topic_info)


