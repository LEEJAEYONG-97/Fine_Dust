from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.ml_model import preprocess_data, make_prediction  # 예측 함수 및 전처리 함수 불러오기
from fastapi.responses import JSONResponse

router = APIRouter()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="app/templates")

# 예측 모델 페이지를 렌더링
@router.get("/predict-model/")
def predict_model_page(request: Request):
    return templates.TemplateResponse("model.html", {"request": request})

# 예측 결과를 처리하는 POST 요청
@router.post("/predict-model/")
def predict_model_result(
    request: Request,
    date: str = Form(...),
    pm25_china_df: float = Form(...),
    pm10_china_df: float = Form(...),
    o3_china_df: float = Form(...),
    no2_china_df: float = Form(...),
    so2_china_df: float = Form(...),
    co_china_df: float = Form(...),
    wind_speed_mps: float = Form(...),
    humidity_percent: float = Form(...)
):
    # 입력 데이터를 전처리
    input_data = preprocess_data(pm25_china_df, pm10_china_df, o3_china_df, no2_china_df, so2_china_df, co_china_df, wind_speed_mps, humidity_percent)

    # 예측 함수 호출
    prediction = make_prediction(input_data)

    # 예측 결과 반환
    return JSONResponse(content={"predictions": prediction})
