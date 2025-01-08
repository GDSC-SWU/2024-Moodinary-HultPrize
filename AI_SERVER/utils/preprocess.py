import os
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

def load_training_data(file_path):
    """
    JSON 파일에서 학습 데이터를 로드합니다.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def train_and_save_model(df, model_path, vectorizer_path, label_encoder_path):
    """
    감정 분류 모델을 학습하고 저장합니다.
    """
    try:
        # 라벨 인코딩
        print("Encoding emotion labels...")
        label_encoder = LabelEncoder()
        df['emotion_label'] = label_encoder.fit_transform(df['emotion'])

        # 학습 데이터 분리
        print("Splitting data into train and test sets...")
        X_train, _, y_train, _ = train_test_split(
            df['text'], df['emotion_label'], test_size=0.2, random_state=42
        )

        # TF-IDF 벡터라이저 학습
        print("Fitting TF-IDF vectorizer...")
        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(X_train)

        # Logistic Regression 모델 학습
        print("Training Logistic Regression model...")
        model = LogisticRegression()
        model.fit(X_train_tfidf, y_train)

        # 모델 저장
        print(f"Saving model to {model_path}...")
        with open(model_path, "wb") as model_file:
            pickle.dump(model, model_file)

        print(f"Saving TF-IDF vectorizer to {vectorizer_path}...")
        with open(vectorizer_path, "wb") as vectorizer_file:
            pickle.dump(vectorizer, vectorizer_file)

        print(f"Saving LabelEncoder to {label_encoder_path}...")
        with open(label_encoder_path, "wb") as label_encoder_file:
            pickle.dump(label_encoder, label_encoder_file)

        print("Model, vectorizer, and label encoder successfully saved!")

    except Exception as e:
        print(f"An error occurred during training or saving: {e}")
