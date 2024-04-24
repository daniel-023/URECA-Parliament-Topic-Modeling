# NTU-URECA-Parliament-Topic-Modeling

## Overview
This repository contains datasets and Python scripts for a natural language processing (NLP) project focused on Singapore's parliamentary debates from 1965 to 1976. The `BERTopic` model, stored with Git Large File Storage (LFS), identifies topics and trends within the historical data to understand the legislative priorities and policy landscape of early Singapore.

## Prerequisites
Before proceeding, ensure you have the following installed:
- Git and Git Large File Storage (LFS)
- Microsoft Visual C++ Build Tools

## Installation Options for BERTopic
When installing Microsoft Visual C++ Build Tools, make sure to select the following options:
- C++ build tools
- Windows 11 SDK
- Latest version of MSVCv143 - VS 2022 C++ x64/x86 build tools

## Installation
Follow these steps to get your development environment running:

1. Clone the repository with Git LFS:
   ```sh
   git clone https://github.com/daniel-023/NTU-URECA-Parliament-Topic-Modeling.git
   ```
2. Navigate to the cloned repository directory:
   ```sh
   cd NTU-URECA-Parliament-Topic-Modeling
   ```
3. Pull the LFS files to retrieve the model:
   ```sh
   git lfs pull
   ```
4. Install the required dependencies from `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```

## Project Structure
- `Datasets/`: Contains reports from the first 3 parliaments of Singapore.
- `Models/`: Stores the trained BERTopic model and embeddings, managed with Git LFS.
- `Output/`: Includes outputs from exploratory data analysis (EDA) and visualizations like the intertopic distance map, document visualizations, and bar charts of top topics.
- `EDA.py`: Script for exploratory data analysis including data information, document length histograms, and word clouds.
- `data_preprocessing.py`: Functions for data loading, cleaning, and preprocessing.
- `topic_modeling.py`: Contains functions for training the BERTopic model, loading models, topic extraction, and visualization.
- `utils.py`: Helper functions for file path building and Excel writing.
- `main.py`: Main script that executes data loading, preprocessing, model training, and visualization.

## Getting Started
1. Clone the repository.
2. Install the required dependencies from `requirements.txt`.
3. Run `main.py` to execute the full pipeline.

## Usage
Details on using individual scripts for specific tasks such as EDA, topic modeling, or visualizations can be found within the respective `.py` files.

## Visualizations
The `Output/` directory contains several visualizations created from the parliamentary datasets:
- **Top Speakers**: Bar charts showing the most frequent speakers in each parliament.
- **Parliament Distribution**: Pie chart showing the distribution of documents across the three parliaments.
- **Document Length Distribution**: Histogram depicting the distribution of document lengths.
- **Word Cloud**: Visual representation of the most common words across all speeches.
- **Intertopic Distance Map**: Visualization of the topic clusters.
- **Document Visualizations**: Plots showing documents clustered by topic.
- **Top Topics Bar Chart**: Bar chart showing the most prevalent topics by document count.
- **Topic Info Table**: HTML table showing detailed topic information.

This project is open-sourced under the [MIT License](LICENSE).
   
