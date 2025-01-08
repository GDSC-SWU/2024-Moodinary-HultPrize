from datetime import datetime
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from app.predict import predict_top5_emotions  # 감정 예측 함수 가져오기

app = FastAPI()

# 데이터 모델 정의
class Diary(BaseModel):
    content: str
    date: Optional[str] = None
    status: str = "pending"  # 기본값 "pending"
    analysis_result: Optional[List[str]] = None  # 고정 키워드 리스트
    emotion: Optional[str] = None  # 분석된 감정

# 임시 저장소
diary_storage: Dict[int, Diary] = {}

# 고정 키워드
DEFAULT_KEYWORDS = [
    "기획안 오류", "파업", "전철 지연", "무기력", "스트레스",
    "사람 붐빔", "발 밟힘", "팀장 히스테리", "이사준비", "자리 뺏김"
]

# 고정 텍스트 파일 경로 수정
TEXT_FILE_DIR = os.path.join(os.path.dirname(__file__), "texts")
TOP_TEXT_FILE = os.path.join(TEXT_FILE_DIR, "top_text.txt")
BOTTOM_TEXT_FILE = os.path.join(TEXT_FILE_DIR, "bottom_text.txt")

# 텍스트 파일 읽기
def read_text_file(file_path: str) -> str:
    """
    고정된 텍스트 파일을 읽어 반환.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"

# 일기 생성
@app.post("/diaries")
def create_diary(diary: Diary):
    """
    새로운 일기를 생성하고 감정 분석 결과를 저장.
    """
    diary_id = len(diary_storage) + 1
    diary.date = datetime.now().strftime("%Y-%m-%d")  # 현재 날짜 설정
    diary.status = "analyzing"  # 상태 변경

    # 감정 분석 수행
    try:
        emotion = predict_top5_emotions(diary.content)  # 감정 예측
        diary.emotion = emotion  # 예측된 감정 저장
        diary.analysis_result = DEFAULT_KEYWORDS  # 고정 키워드 저장
        diary.status = "completed"  # 상태 완료로 변경
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    # 저장소에 일기 추가
    diary_storage[diary_id] = diary
    return {"id": diary_id, "message": "Diary created and analyzed successfully"}


# 키워드 리스트 반환
@app.get("/diaries/completed_list")
def get_completed_diaries():
    """
    완료된 모든 일기의 키워드 리스트 반환.
    """
    completed_diaries = [
        {
            "id": diary_id,
            "user": "은지",
            "keywords": diary.analysis_result
        }
        for diary_id, diary in diary_storage.items()
        if diary.status == "completed"
    ]
    
    if not completed_diaries:
        raise HTTPException(status_code=404, detail="No completed diaries found")
    
    return {"message": "Completed diaries fetched successfully", "data": completed_diaries}



# 분석 완료된 일기 페이지 반환
@app.get("/diaries/{diary_id}/completed_page")
def get_completed_page(diary_id: int):
    """
    분석이 완료된 일기의 상세 페이지 반환.
    """
    diary = diary_storage.get(diary_id)

    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    if diary.status != "completed":
        raise HTTPException(status_code=400, detail="Diary analysis not completed")

    # 고정 텍스트 읽기
    top_text = read_text_file(TOP_TEXT_FILE)
    bottom_text = read_text_file(BOTTOM_TEXT_FILE)

    return {
        "date": diary.date,
        "user": "은지",  # 고정된 사용자 이름
        "content": diary.content,  # 입력된 content 추가
        "emotion": diary.emotion,
        "keywords": diary.analysis_result,
        "top_text": top_text,
        "bottom_text": bottom_text,
    }


