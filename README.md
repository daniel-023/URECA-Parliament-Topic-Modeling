# NTU URECA Parliament Topic Modeling

## Overview
This repository contains datasets and Python scripts for a natural language processing (NLP) project focused on Singapore's parliamentary debates from 1965 to 1976. The `BERTopic` model identifies topics and trends within the historical data to understand the legislative priorities and policy landscape of early Singapore.

## Data Preview
| parliament  | sitting_date | title | MPs_speaking | main_text | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | 24/1/1968 | REDUNDANCY PAYMENTS FUND BILL | Mr Jek Yeun Thong (Minister for Labour); Mr Lee Kuan Yew (Prime Minister); Inche Mohd. Ariff Bin Suradi; Mr Bernard Rodrigues; Mr Ho See Beng; Mr P. Govindaswamy; Mr P. Selvadurai; Mr Teong Eng Siong; Mr P. Coomaraswamy (Mr Speaker); | Hon. Members are already aware that the withdrawal of British forces from Singapore will render a large number of workers unemployed. The House has just heard a statement by the Prime Minister that the British have again notified us that they will further cut short their stay and that they will be completely out by the end of 1971. | 

## Requirements
- Python 3.12.1
- Microsoft Visual C++ Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

## Installation Options for BERTopic
When installing Microsoft C++ Build Tools, make sure to select the following options:
- Windows 10/11 SDK
- MSVCv143 - VS 2022 C++ x64/x86 build tools (Latest)

## Project Set-up
Follow these steps to get your development environment running:

1. Clone the repository:
   ```sh
   git clone https://github.com/daniel-023/NTU-URECA-Parliament-Topic-Modeling.git
   ```

2. Navigate to the cloned repository directory:
   ```sh
   cd NTU-URECA-Parliament-Topic-Modeling
   ```

3. Create a virtual environment:
   ```sh
   python -m venv myenv
   ```
   Activate the virtual environment (PowerShell)
   ```sh
   myenv/Scripts/activate.ps1
   ```

5. Install the required dependencies from `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```

## Project Structure
- [Datasets](./Datasets/): Contains reports from the first 3 parliaments of Singapore.
- [Models](./Models/): Stores the trained BERTopic model and embeddings
- [Output](./Output/): Includes outputs from exploratory data analysis (EDA) and visualisations like the intertopic distance map, document visualisations, and bar charts of top topics.
- [EDA.py](./EDA.py/): Script for exploratory data analysis including data information, document length histograms, and word clouds.
- [data_preprocessing.py](./data_preprocessing.py/): Functions for data loading, cleaning, and preprocessing.
- [topic_modeling.py](./topic_modeling.py/): Contains functions for training the BERTopic model, loading models, topic extraction, and visualisation.
- [utils.py](./utils.py/): Helper functions for file path building and Excel writing.
- [main.py](./main.py/): Main script that executes data loading, preprocessing, model training, and visualisation.
- [predict.py](./predict.py/): Script for predicting topics of unseen text using the trained BERTopic model.
- [app.py](./app.py/): Streamlit app containing topic visualisation and topic prediction tools

## Visualisations
The `Output/` directory contains several visualisations created from the parliamentary datasets:
- **Top 10 Speakers**: Bar charts showing the most frequent speakers in each parliament.
- **Parliament Distribution**: Pie chart showing the distribution of documents across the three parliaments.
- **Document Length Distribution**: Histogram depicting the distribution of document lengths.
- **Word Cloud**: Visual representation of the most common words across all speeches.
- **Intertopic Distance Map**: Visualisation of the topic clusters.
- **Document Visualisations**: Plots showing documents clustered by topic.
- **Top 5 Topics Bar Chart**: Bar chart showing the most prevalent topics by document count.
- **Topic Info Table**: HTML table showing detailed topic representations.

This project is open-sourced under the [MIT License](LICENSE).
   
