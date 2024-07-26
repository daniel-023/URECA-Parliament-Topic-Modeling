import streamlit as st
from sentence_transformers import SentenceTransformer
from topic_modeling import load_model

# Load the model
model = load_model("Parliament_Topic_Model")

# Streamlit app title
st.title("Topic Modeling with Sentence Transformers")

# Input text area
user_input = st.text_area("Enter text for topic modeling:", height=300)

if st.button("Analyze"):
    if user_input:
        # Load the embedding model
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Generate embeddings
        embeddings = embedding_model.encode([user_input], show_progress_bar=True)

        # Perform topic modeling
        new_topics, new_probs = model.transform([user_input], embeddings)

        # Custom topic names
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
            16: 'Public Health',
            17: 'Fire and Emergency Services',
            18: 'Market and Hawker Licensing'
        }

        # Display results
        for topic, prob in zip(new_topics, new_probs):
            topic_name = custom_topic_names.get(topic, "Unknown")
            st.write(f"Predicted Topic: {topic_name}, Confidence: {prob:.2f}")
    else:
        st.write("Please enter some text for analysis.")