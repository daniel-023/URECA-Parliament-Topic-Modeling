from bertopic import BERTopic
import joblib
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from umap import UMAP
from utils import *


# Model Training - Stores trained model and embeddings in ./models
def train_model(data, model_name):
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = generate_embeddings(data)
    vectorizer_model = CountVectorizer(ngram_range=(1, 3), stop_words="english")
    topic_model = BERTopic(vectorizer_model=vectorizer_model, min_topic_size=10, nr_topics=20).fit(data, embeddings)
    topic_model.save(build_file_path("models", f'{model_name}.joblib'))
    model_path = build_file_path('models', f'{model_name}_embeddings.joblib')
    with open(model_path, 'wb') as file:
        joblib.dump(embeddings, file)


# Generate Embeddings - Stores embeddings in ./models
def generate_embeddings(data):
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = sentence_model.encode(data, show_progress_bar=True)
    model_path = build_file_path('models', f'{"Parliament_Topic_Model"}_embeddings.joblib')
    with open(model_path, 'wb') as file:
        joblib.dump(embeddings, file)


# Load model stored in local directory
def load_model(model_name):
    model_path = build_file_path('models', f'{model_name}.joblib')
    if os.path.exists(model_path):
        loaded_model = BERTopic.load(model_path)
        return loaded_model
    else:
        raise FileNotFoundError(f"Model file not found at {model_path}")


# Load embeddings stored in local directory
def load_embeddings(model_name):
    embeddings_path = build_file_path('models', f'{model_name}_embeddings.joblib')
    if os.path.exists(embeddings_path):
        with open(embeddings_path, 'rb') as file:
            embeddings = joblib.load(file)
            return embeddings
    else:
        raise FileNotFoundError(f"Embeddings file not found at {embeddings_path}")


def topic_extraction(loaded_model):
    topic_info = loaded_model.get_topic_info().set_index('Topic')[['Count', 'Name', 'Representation']]
    return topic_info


def assign_topic_names(topic_info, custom_names):
    for topic_num in topic_info.index:
        if topic_num in custom_names:
            topic_info.at[topic_num, 'Name'] = custom_names[topic_num]


def export_topic_info(topic_info):
    topic_info.to_html(build_file_path('Output', 'topic_info_table.html'))


def intertopic_distance_map(loaded_model):
    loaded_model.visualize_topics().write_html(build_file_path('Output', 'Intertopic_Distance_Map.html'))


def top_keywords_bar(loaded_model):
    fig = loaded_model.visualize_barchart(top_n_topics=20)
    fig.write_html(build_file_path('Output', 'top_topic_keywords.html'))


def visualise_documents(data, loaded_model, embeddings):
    loaded_model.visualize_documents(data, embeddings=embeddings)
    reduced_embeddings = UMAP(n_neighbors=10, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    (loaded_model.visualize_documents(data, reduced_embeddings=reduced_embeddings)
     .write_html(build_file_path('Output', 'Document_Visualisations.html')))


def visualize_top_topics(topic_info, top_n=5):
    filtered_topic_info = topic_info[1:]
    top_topics = filtered_topic_info.sort_values(by='Count', ascending=False).head(top_n)
    plt.figure(figsize=(12, 8))
    plt.barh(top_topics['Name'], top_topics['Count'], color='grey')
    plt.xlabel('Volume (Number of Documents)')
    plt.ylabel('Topics')
    plt.title(f'Top {top_n} Topics by Volume')
    plt.xticks(fontsize=12)  # Increase x-axis tick font size here
    plt.yticks(fontsize=16)
    plt.gca().invert_yaxis()  # Invert the y-axis to have the highest count on top
    plt.tight_layout()
    plt.savefig(build_file_path('Output', 'top_topics_bar.png'))
