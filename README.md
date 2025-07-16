# 🐦 Twitter Emotion Detection using DVC Pipelines

This project builds an end-to-end machine learning pipeline to classify tweets into emotional categories (specifically **happiness** and **sadness**) using the Bag-of-Words approach and XGBoost. The entire pipeline is tracked and orchestrated using **DVC** (Data Version Control).

> 🎥 Tutorial followed: [DS with Bappy — ML Pipeline with DVC](https://www.youtube.com/watch?v=w71RHxAWxaM&t=8950s)
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

