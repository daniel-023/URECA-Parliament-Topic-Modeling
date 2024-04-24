from data_preprocessing import *
from EDA import *
from topic_modeling import *

# Loading and combining data
df = combine_data('Parl_1.csv', 'Parl_2.csv', 'Parl_3.csv')

df['main_text'] = df['main_text'].apply(preprocess_text)

df['doc_length'] = doc_length_col(df)

df = length_filter(df, 200)

# length_distribution_hist(df, 'Output', 'doc_length_distribution.png')

print(data_info(df))

# word_cloud(df, 'Output', 'wordcloud.png')

# speaker_frequency_bar(df, 1, 'Output', 'Parl1_Top10_Speakers')
# speaker_frequency_bar(df, 2, 'Output', 'Parl2_Top10_Speakers')
# speaker_frequency_bar(df, 3, 'Output', 'Parl3_Top10_Speakers')

# parl_distribution(df, 'output', 'Parl_Distribution.png')

# train_model(df['main_text'], 'Parliament Topic Model')

loaded_model = load_model('Parliament Topic Model')

topic_info = topic_extraction(loaded_model)

custom_topic_names = {
    0: 'Education System',
    1: 'Legislative and Legal Framework',
    2: 'Public Transport and Infrastructure',
    3: 'Property and Housing Taxation',
    4: 'National Identity and Immigration',
    5: 'Financial Policy and Budgeting',
    6: 'Urban Planning and Land Use',
    7: 'Labour and Industrial Relations',
    8: 'Cultural Programmes and Media',
    9: 'Foreign Relations and Economic Policy',
    10: 'Agricultural Development',
    11: 'Family Planning and Womens\' Health',
    12: 'Airport Operations and Development',
    13: 'Sports and National Events',
    14: 'Drugs and Pharmaceutical Regulations',
    15: 'Public Health and Sanitation',
    16: 'Fire Safety and Emergency Services',
    17: 'Food Safety and Market Regulations',
    18: 'Social Security and Welfare'
}

assign_topic_names(topic_info, custom_topic_names)

export_topic_info(topic_info)

intertopic_distance_map(loaded_model)

embeddings = load_embeddings('Parliament Topic Model')

visualise_documents(df['main_text'], loaded_model, embeddings=embeddings)

visualize_top_topics(topic_info)

