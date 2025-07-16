# 🐦 Twitter Emotion Detection using DVC Pipelines

This project builds an end-to-end machine learning pipeline to classify tweets into emotional categories (specifically **happiness** and **sadness**) using the Bag-of-Words approach and XGBoost. The entire pipeline is tracked and orchestrated using **DVC** (Data Version Control).

> 🎥 Tutorial followed: [DS with Bappy — ML Pipeline with DVC](https://www.youtube.com/watch?v=w71RHxAWxaM&t=8950s)
---
## 📂 Project Structure
.
├── data/                       # Raw, processed, and feature data (DVC-tracked)
│   ├── raw/                    # Original data split (train/test)
│   ├── processed/              # Cleaned and preprocessed tweets
│   └── features/               # Bag-of-Words transformed data
│
├── src/                        # Modular Python scripts
│   ├── data_ingestion.py       # Downloads and filters the dataset
│   ├── data_preprocessing.py   # Text cleaning and normalization
│   ├── feature_engineering.py  # Bag-of-Words transformation
│   ├── model_training.py       # XGBoost model training
│   └── evaluate.py             # Model evaluation and metric logging
│
├── twitter_emotion_detection.ipynb   # Interactive notebook version of the pipeline
├── dvc.yaml                   # DVC pipeline stage definitions
├── dvc.lock                   # Auto-generated lock file with exact inputs/outputs
├── model.pkl                  # Trained XGBoost model (DVC output)
├── metrics.json               # Evaluation metrics (accuracy, precision, recall, etc.)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files and folders to ignore in Git
└── README.md                  # Project documentation


---

## 📊 Dataset

- Source: [`tweet_emotions.csv`](https://raw.githubusercontent.com/entbappy/Branching-tutorial/refs/heads/master/tweet_emotions.csv)
- Task: Binary classification of tweet sentiment (`happiness` = 1, `sadness` = 0)

---

## 🚀 Pipeline Stages

This project uses modular components and defines them in a reproducible DVC pipeline:

| Stage               | Description                                |
|---------------------|--------------------------------------------|
| `data_ingestion`    | Downloads and filters the dataset          |
| `data_preprocessing`| Cleans and normalizes the tweets           |
| `feature_engineering` | Applies Bag-of-Words vectorization       |
| `model_training`    | Trains XGBoost classifier                  |
| `model_evaluation`  | Evaluates and logs metrics                 |

---

