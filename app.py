import os
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from data_preprocessing import preprocess_text
from EDA import parl_distribution, reports_over_time, word_cloud

@st.cache_resource
def load_topic_model():
    model = BERTopic.load("daniel-023/Parliament_Topic_Model")
    model.set_topic_labels(custom_topic_names)
    return model

# Function to handle side bar text selection from txt file
def set_text(text):
    st.session_state['user_input'] = text

@st.cache_data
def read_files(filename):
    with open(f'./sample_texts/{filename}', 'r') as f:
            text = f.read()
    return text

@st.cache_data(max_entries=10)
def get_embeddings(user_input):
    embeddings = embedding_model.encode([user_input], show_progress_bar=True)
    return embeddings

@st.cache_data
def generate_wordcloud(df):
    fig = word_cloud(df)
    return fig

df = pd.read_excel('Datasets/parl_data.xlsx')

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

# Load the model
model = load_topic_model()
 # Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit app title
st.title("Parliament Topic Modeling")

# Sidebar
page = st.sidebar.selectbox("Choose a page", ["Exploratory Data Analysis", "Intertopic Distance Map", "Topic Keywords", "Topic Prediction",])

# Initialize session state for user input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

sample_directory = 'sample_texts'
files = os.listdir(sample_directory)

sample_dictionary = {}
for file in files:
    sample_dictionary[file] = read_files(file)


if page == "Exploratory Data Analysis":
    st.header("Exploratory Data Analysis")
    fig = parl_distribution(df)
    st.plotly_chart(fig)

    fig = reports_over_time(df)
    st.plotly_chart(fig)

    st.pyplot(generate_wordcloud(df))

    del df


elif page == "Intertopic Distance Map":
    st.header("Intertopic Distance Map")
    st.write("""
This intertopic distance map visualises the relationships between different topics identified by the model.
Each circle represents a topic, and the size of the circle indicates the prevalence of the topic in the corpus.
The distance between circles represents how semantically similar or different the topics are from each other.
You can hover over each circle to see the top words associated with that topic.
""")
    
    fig = model.visualize_topics()
    st.plotly_chart(fig, use_container_width=True)

elif page == "Topic Keywords":
    st.header("Topic Keywords")
    st.write("""
This barchart visualises the top keywords for each topic identified by the model. 
Each bar represents a keyword, and the length of the bar indicates the importance or relevance of that keyword to the topic.
You can hover over each bar to see the exact score of the keyword.
""")
    
    chart = model.visualize_barchart(custom_labels=False, top_n_topics=20)
    st.plotly_chart(chart)

elif page == "Topic Prediction":
    st.sidebar.header("Sample Texts")
    st.write("""
This page allows you to enter text and analyse it using the BERTopic model. 
You can either type your own text or use one of the provided sample texts. 
When you click the "Analyse" button, the model will predict the most relevant topic for the input text and display the topic name, topic number, and confidence score.
""")

    for label, text in sample_dictionary.items():
        st.sidebar.button(label.split('.')[0], on_click=set_text, args=(text, ))

    # Input text area
    user_input = st.text_area("Enter text for topic modeling:", st.session_state['user_input'], height=300)

    if st.button("Analyse"):
        if user_input:
            # Generate embeddings
            embeddings = get_embeddings(user_input)

            # Perform topic modeling
            new_topics, new_probs = model.transform([user_input], embeddings) 
            
            # Display results
            for topic, prob in zip(new_topics, new_probs):
                topic_name = custom_topic_names.get(topic, "Unknown Topic")
                st.write(f"Predicted Topic: {topic_name}, Topic Number: {topic}, Confidence: {prob:.2f}")
            del embeddings
        
        else:
            st.write("Please enter some text for analysis.")
    
    
    