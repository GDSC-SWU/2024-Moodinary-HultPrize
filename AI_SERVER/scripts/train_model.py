from utils.preprocess import train_and_save_model, load_training_data

if __name__ == "__main__":
    # 데이터 로드
    print("Loading training data...")
    data_path = "./data/training_merged_data.json"
    df = load_training_data(data_path)

    # 모델 저장 경로
    model_path = "./models/logistic_model.pkl"
    vectorizer_path = "./models/tfidf_vectorizer.pkl"
    label_encoder_path = "./models/label_encoder.pkl"

    # 모델 학습 및 평가
    train_and_save_model(df, model_path, vectorizer_path, label_encoder_path)
