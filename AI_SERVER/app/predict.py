# import os
# import joblib
# import numpy as np
# import json

# # 현재 디렉토리 기준 경로 설정
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # 모델, 벡터화기, 라벨 인코더 로드
# vectorizer = joblib.load(os.path.join(BASE_DIR, "models/tfidf_vectorizer.pkl"))
# model = joblib.load(os.path.join(BASE_DIR, "models/logistic_model.pkl"))
# label_encoder = joblib.load(os.path.join(BASE_DIR, "models/label_encoder.pkl"))

# # 감정 라벨 매핑 로드
# with open(os.path.join(BASE_DIR, "data/emotion_mapping.json"), "r", encoding="utf-8") as f:
#     emotion_mapping = json.load(f)

# # 감정 예측 함수
# def predict_top5_emotions(input_text: str) -> list:
#     # 입력 텍스트를 벡터화
#     input_tfidf = vectorizer.transform([input_text])
#     # 모델을 사용하여 감정 확률 예측
#     probabilities = model.predict_proba(input_tfidf)[0]
#     # 상위 5개 확률의 인덱스 추출
#     top5_indices = np.argsort(probabilities)[::-1][:5]
#     # 감정 라벨 추출
#     top5_emotions = [label_encoder.inverse_transform([i])[0] for i in top5_indices]
#     # 라벨을 한글로 변환
#     top5_emotions_korean = [emotion_mapping.get(emotion, "Unknown") for emotion in top5_emotions]
#     return top5_emotions_korean
import os
import joblib
import numpy as np
import json

# 현재 디렉토리 기준 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 모델, 벡터화기, 라벨 인코더 로드
vectorizer = joblib.load(os.path.join(BASE_DIR, "models/tfidf_vectorizer.pkl"))
model = joblib.load(os.path.join(BASE_DIR, "models/logistic_model.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "models/label_encoder.pkl"))

# 감정 라벨 매핑 로드
with open(os.path.join(BASE_DIR, "data/emotion_mapping.json"), "r", encoding="utf-8") as f:
    emotion_mapping = json.load(f)

# 감정 예측 함수
def predict_top5_emotions(input_text: str) -> str:
    """
    입력 텍스트에서 상위 5개의 감정을 예측한 후, 5번째 감정을 반환합니다.
    부족할 경우 기본값으로 '분노'를 반환합니다.
    """
    # 입력 텍스트를 벡터화
    input_tfidf = vectorizer.transform([input_text])
    
    try:
        # 모델을 사용하여 감정 확률 예측
        probabilities = model.predict_proba(input_tfidf)[0]
        # 상위 5개 확률의 인덱스 추출
        top5_indices = np.argsort(probabilities)[::-1][:5]
        # 감정 라벨 추출
        top5_emotions = [label_encoder.inverse_transform([i])[0] for i in top5_indices]
        # 라벨을 한글로 변환
        top5_emotions_korean = [emotion_mapping.get(emotion, "Unknown") for emotion in top5_emotions]
    except Exception:
        # 예외 발생 시 기본값 반환
        return "분노"

    # 5개의 감정을 예측하지 못하면 기본값 "분노" 반환
    if len(top5_emotions_korean) < 5:
        return "분노"

    # 3번째 감정 반환
    return top5_emotions_korean[-3]
