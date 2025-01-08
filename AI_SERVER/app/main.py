from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict_top5_emotions  # 감정 예측 함수 가져오기

# FastAPI 객체 생성
app = FastAPI()

# 입력 데이터 모델 정의
class InputText(BaseModel):
    text: str

# API 엔드포인트 정의
@app.post("/predict")
def predict_emotion(input_data: InputText):
    # 입력 텍스트로 감정 예측 수행
    top5_emotions = predict_top5_emotions(input_data.text)
    # 5번째 감정을 추출
    fifth_emotion = top5_emotions[-1]
    return {
        # "top5_emotions": top5_emotions,  # 상위 5개 감정
        "fifth_emotion": fifth_emotion   # 5번째 감정
    }
