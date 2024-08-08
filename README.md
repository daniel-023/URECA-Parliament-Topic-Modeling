# NTU URECA Parliament Topic Modeling

## Overview
This repository contains datasets and Python scripts for a natural language processing (NLP) project focused on Singapore's parliamentary debates from 1965 to 1976. The `BERTopic` model identifies topics and trends within the historical data to understand the legislative priorities and policy landscape of early Singapore.

[Interactive Streamlit App](https://ureca-parliament-topic-modeling.streamlit.app/)

![](https://github.com/daniel-023/NTU-URECA-Parliament-Topic-Modeling/blob/main/visualisations/Intertopic_Distance_Map.gif)

## Data Preview
| parliament  | sitting_date | title | MPs_speaking | main_text | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | 24/1/1968 | REDUNDANCY PAYMENTS FUND BILL | Mr Jek Yeun Thong (Minister for Labour); Mr Lee Kuan Yew (Prime Minister); Inche Mohd. Ariff Bin Suradi; Mr Bernard Rodrigues; Mr Ho See Beng; Mr P. Govindaswamy; Mr P. Selvadurai; Mr Teong Eng Siong; Mr P. Coomaraswamy (Mr Speaker); | Hon. Members are already aware that the withdrawal of British forces from Singapore will render a large number of workers unemployed. The House has just heard a statement by the Prime Minister that the British have again notified us that they will further cut short their stay and that they will be completely out by the end of 1971. |
| 2 | 2/6/1972 | DANGEROUS FIREWORKS BILL | Prof. Wong Lin Ken (Minister for Home Affairs); | The Minor Offences (Amendment) Act, 1970, came into operation on 19th June, 1970. Since then the general prohibition had been lifted for five days during the Chinese New Year festival of 1971, and for another five days for the same festival in 1972. |
| 3 | 24/11/1976 | TAN WAH PIOW (Entry into Britain) | Mr Chua Sian Chin; Mr Ho See Beng; Mr J. F. Conceicao; Mr Ng Kah Ting; Mr P. Govindaswamy; Mr P. Selvadurai; | Mr P. Selvadurai asked the Minister for Home Affairs and Education if he will enlighten this House as to how Mr Tan Wah Piow, who had absconded  before reporting for National Service, managed to enter Britain; whether Mr Tan had valid travel documents. and if so, how were they acquired, if not, how was he allowed entry into Britain in June. 1976; and what action, if any, the Government intends to take against Mr Tan. |

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
![](https://github.com/daniel-023/NTU-URECA-Parliament-Topic-Modeling/blob/main/visualisations/flag_wordcloud.png)
The `Output/` directory contains several visualisations created from the parliamentary datasets:
**EDA**
- **Parliament Distribution**: Bar chart showing the distribution of documents across the three parliaments.
- **Number of Sessions over Time**: Line chart showing the distribution of parliament sessions per month.
- **Word Cloud**: Visual representation of the most common words across parliament report titles.
- **Top 10 Speakers**: Bar charts showing the most frequent speakers in each parliament.
- **Document Length Distribution**: Histogram depicting the distribution of document lengths.

**Topic Modeling**
- **Intertopic Distance Map**: Visualisation of the topic clusters.
- **Document Visualisations**: Plots showing documents clustered by topic.
- **Top 5 Topics Bar Chart**: Bar chart showing the most prevalent topics by document count.
- **Topic Info Table**: HTML table showing detailed topic representations.

This project is open-sourced under the [MIT License](LICENSE).
   
