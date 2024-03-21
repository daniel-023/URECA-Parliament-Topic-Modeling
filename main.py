from data_preprocessing import combine_data, preprocess_text

# Loading and combining data
df = combine_data('Parl_1.csv', 'Parl_2.csv')

# Preprocessing text
df['main_text'] = df.apply('main_text').apply(lambda x: preprocess_text(x))
