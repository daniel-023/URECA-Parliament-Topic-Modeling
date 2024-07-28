from sentence_transformers import SentenceTransformer
from topic_modeling import load_model


model = load_model("Parliament_Topic_Model")

user_input = [input("Enter text here to identify topic: ")]

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedding_model.encode(user_input, show_progress_bar=True)

print(embeddings)
new_topics, new_probs = model.transform(user_input, embeddings)

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

for topic, prob in zip(new_topics, new_probs):
    topic_name = custom_topic_names.get(topic)
    print(f"Predicted Topic: {topic_name}, Confidence: {prob}")