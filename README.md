# NTU URECA Parliament Topic Modeling

<a href="https://ureca-parliament-topic-modeling.streamlit.app/">
  <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit">
</a>


## 🛠 Overview
This project applies Natural Language Processing (NLP) techniques to analyze Singapore's parliamentary debates between 1965 and 1976. Using the `BERTopic` model, we uncover topics and trends in the legislative priorities of early Singapore, contributing to a deeper understanding of the political and policy landscape during this period.

![Intertopic Distance Map](https://github.com/daniel-023/URECA-Parliament-Topic-Modeling/blob/main/visualisations/Intertopic_Distance_Map.gif)


## 🎯 Key Features
* **Topic Modeling:** Using BERTopic to extract topics from historical parliamentary data.
* **Data Visualization:** Interactive charts such as intertopic distance maps, word clouds, and document clusters.
* **Exploratory Data Analysis (EDA):** Comprehensive analysis of the parliamentary reports from three early parliaments of Singapore.
* **Interactive App:** Access the Streamlit app to visualize and explore the data interactively.


## 🔍 Data Preview
| **parliament**  | **sitting_date** | **title** | **MPs_speaking** | **main_text** | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | 24/1/1968 | REDUNDANCY PAYMENTS FUND BILL | Mr Jek Yeun Thong (Minister for Labour); Mr Lee Kuan Yew (Prime Minister); Inche Mohd. Ariff Bin Suradi; Mr Bernard Rodrigues; Mr Ho See Beng; Mr P. Govindaswamy; Mr P. Selvadurai; Mr Teong Eng Siong; Mr P. Coomaraswamy (Mr Speaker); | Hon. Members are already aware that the withdrawal of British forces from Singapore will render a large number of workers unemployed. The House has just heard a statement by the Prime Minister that the British have again notified us that they will further cut short their stay and that they will be completely out by the end of 1971. |
| 2 | 2/6/1972 | DANGEROUS FIREWORKS BILL | Prof. Wong Lin Ken (Minister for Home Affairs); | The Minor Offences (Amendment) Act, 1970, came into operation on 19th June, 1970. Since then the general prohibition had been lifted for five days during the Chinese New Year festival of 1971, and for another five days for the same festival in 1972. |
| 3 | 24/11/1976 | TAN WAH PIOW (Entry into Britain) | Mr Chua Sian Chin; Mr Ho See Beng; Mr J. F. Conceicao; Mr Ng Kah Ting; Mr P. Govindaswamy; Mr P. Selvadurai; | Mr P. Selvadurai asked the Minister for Home Affairs and Education if he will enlighten this House as to how Mr Tan Wah Piow, who had absconded  before reporting for National Service, managed to enter Britain; whether Mr Tan had valid travel documents. and if so, how were they acquired, if not, how was he allowed entry into Britain in June. 1976; and what action, if any, the Government intends to take against Mr Tan. |


## 🚀 Quick Start
1. Clone the Repository:
   ```sh
   git clone https://github.com/daniel-023/URECA-Parliament-Topic-Modeling.git
   ```

2. Navigate to the Project Directory:
   ```sh
   cd URECA-Parliament-Topic-Modeling
   ```

3. Set Up Virtual Environment:
   ```sh
   python -m venv myenv
   ```
   Activate it (for PowerShell)
   ```sh
   myenv/Scripts/activate.ps1
   ```

5. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Run the Application:
   ```sh
   streamlit run app.py
   ```


## 📂 Project Structure
```
URECA-Parliament-Topic-Modeling/
│
├── Datasets/               # Original parliamentary reports from 1965-1976
├── Models/                 # BERTopic model and embeddings
├── Output/                 # Visualizations, charts, and generated outputs
├── EDA.py                  # Exploratory Data Analysis
├── data_preprocessing.py   # Data loading, cleaning, and preprocessing scripts
├── topic_modeling.py       # BERTopic modeling and visualization
├── utils.py                # Helper functions
├── main.py                 # Main script for running the pipeline
└── app.py                  # Streamlit application for topic modeling and prediction
```


## 🔧 Installation Notes
For Windows users, you will need to install the **[Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)** before installing BERTopic. Ensure the following components are selected:

* **Windows 10/11 SDK**
* **MSVCv143 - VS 2022 C++ x64/x86 build tools (Latest)**

  
## 📊 Visualisations
![](https://github.com/daniel-023/URECA-Parliament-Topic-Modeling/blob/main/Output/singapore_flag_wordcloud.png)
The `Output/` folder contains several visualizations generated from the parliamentary data:

* **Intertopic Distance Map:** Explore the clustering of topics.
* **Document Clusters:** Visual representation of documents grouped by topic. 
* **Word Clouds:** Visualize the most frequently occurring words in parliament debates.  
* **Top 10 Speakers:** Bar charts depicting the most frequent speakers by parliament. 
* **Document Length Distribution:** Histogram of document lengths.

  
## 💻 Requirements
* Python 3.12.1
* Microsoft Visual C++ Build Tools

  
## 🔗 Links
* [Streamlit App](https://ureca-parliament-topic-modeling.streamlit.app/)

  
This project is open-sourced under the [MIT License](LICENSE).
