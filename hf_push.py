from topic_modeling import load_model
from huggingface_hub import login

# login()

model = load_model("Parliament_Topic_Model")
model.push_to_hf_hub('daniel-023/parliament_topic_model')


