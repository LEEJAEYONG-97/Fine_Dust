from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import dashboard, predict_model  # 라우터 임포트

# FastAPI 애플리케이션 생성
app = FastAPI()

# 정적 파일 경로 설정 (CSS, JavaScript 등)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 라우터 추가: dashboard.py의 라우터를 포함하여 '/' 경로를 처리
app.include_router(dashboard.router)

# 새로운 예측 경로 추가 (ml_model.py)
app.include_router(predict_model.router)  # ml_model 라우터 추가

# 루트 엔드포인트
@app.get("/")
def read_root():
    return {"message": "미세먼지 Project"}