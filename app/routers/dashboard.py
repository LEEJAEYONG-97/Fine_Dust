from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
# 연평균, 월평균, 계절별 데이터 로드 함수 불러오기
from app.data_handler import load_yearly_avg_data, load_monthly_avg_data, load_seasonal_avg_data, load_monthly_weather

router = APIRouter()

# 템플릿 설정 (템플릿 파일이 있는 디렉토리를 설정)
templates = Jinja2Templates(directory="app/templates")

# 한국과 중국의 PM2.5, PM10 연평균, 월평균, 계절별 평균 및 날씨 데이터를 대시보드에 표시하는 엔드포인트
@router.get("/")
async def show_dashboard(request: Request):
    # 1. 한국과 중국 데이터 파일 경로 설정
    kor_file = "data/kor_combined_file.csv"  # 한국 데이터 파일 경로
    cha_file = "data/cha_combined_file.csv"  # 중국 데이터 파일 경로
    weather_file = "data/kor_weather.csv"    # 한국 날씨 데이터 파일 경로
    
    # 2. 연평균 데이터 로드
    kor_yearly_avg, cha_yearly_avg = load_yearly_avg_data(kor_file, cha_file)
    #    -> 연도별 PM2.5 및 PM10 평균 데이터를 로드하여 사용
    #    -> 각 연도의 PM2.5, PM10 평균 데이터를 한국과 중국에 대해 구분
    
    # 3. 월평균 데이터 로드
    kor_monthly_avg, cha_monthly_avg = load_monthly_avg_data(kor_file, cha_file)
    #    -> 월별 PM2.5 및 PM10 평균 데이터를 로드하여 사용
    #    -> 각 월의 PM2.5, PM10 평균 데이터를 한국과 중국에 대해 구분

    # 4. 계절별 데이터 로드
    kor_seasonal_avg, cha_seasonal_avg = load_seasonal_avg_data(kor_file, cha_file)
    #    -> 계절별 PM2.5 및 PM10 평균 데이터를 로드하여 사용
    #    -> 봄, 여름, 가을, 겨울에 해당하는 PM2.5, PM10 데이터를 한국과 중국에 대해 구분

    # 5. 연평균 PM2.5 데이터를 딕셔너리로 변환
    pm25_data = {
        'korea': kor_yearly_avg['pm25'].tolist(),  # 한국의 PM2.5 연평균 리스트 (2015~2023)
        'china': cha_yearly_avg['pm25'].tolist(),  # 중국의 PM2.5 연평균 리스트 (2015~2023)
        'year': kor_yearly_avg['year'].tolist()    # 연도 리스트 (2015~2023)
    }

    # 6. 연평균 PM10 데이터를 딕셔너리로 변환
    pm10_data = {
        'korea': kor_yearly_avg['pm10'].tolist(),  # 한국의 PM10 연평균 리스트 (2015~2023)
        'china': cha_yearly_avg['pm10'].tolist(),  # 중국의 PM10 연평균 리스트 (2015~2023)
        'year': kor_yearly_avg['year'].tolist()    # 연도 리스트 (2015~2023)
    }

    # 7. 월평균 PM2.5 데이터를 딕셔너리로 변환
    pm25_monthly_data = {
        'korea': kor_monthly_avg['pm25'].tolist(),  # 한국의 월별 PM2.5 평균 리스트 (1~12월)
        'china': cha_monthly_avg['pm25'].tolist(),  # 중국의 월별 PM2.5 평균 리스트 (1~12월)
        'month': kor_monthly_avg['month'].tolist()  # 월 리스트 (1월 ~ 12월)
    }

    # 8. 월평균 PM10 데이터를 딕셔너리로 변환
    pm10_monthly_data = {
        'korea': kor_monthly_avg['pm10'].tolist(),  # 한국의 월별 PM10 평균 리스트 (1~12월)
        'china': cha_monthly_avg['pm10'].tolist(),  # 중국의 월별 PM10 평균 리스트 (1~12월)
        'month': kor_monthly_avg['month'].tolist()  # 월 리스트 (1월 ~ 12월)
    }

    # 9. 계절별 PM2.5 데이터를 딕셔너리로 변환
    pm25_season_data = {
        'korea': kor_seasonal_avg['pm25'].tolist(),  # 한국의 계절별 PM2.5 평균 리스트
        'china': cha_seasonal_avg['pm25'].tolist(),  # 중국의 계절별 PM2.5 평균 리스트
        'season': kor_seasonal_avg['season'].tolist()  # 계절 리스트 (봄, 여름, 가을, 겨울)
    }

    # 10. 계절별 PM10 데이터를 딕셔너리로 변환
    pm10_season_data = {
        'korea': kor_seasonal_avg['pm10'].tolist(),  # 한국의 계절별 PM10 평균 리스트
        'china': cha_seasonal_avg['pm10'].tolist(),  # 중국의 계절별 PM10 평균 리스트
        'season': kor_seasonal_avg['season'].tolist()  # 계절 리스트 (봄, 여름, 가을, 겨울)
    }

    # 11. 월별 습도 및 풍속 데이터 로드
    weather_data = load_monthly_weather(weather_file)
    #    -> 월별 습도 및 풍속 데이터를 로드하여 사용
    #    -> 한국의 월별 습도와 풍속 데이터를 시각화

    # 12. 날씨 데이터를 딕셔너리로 변환
    weather_data = {
        'humidity': weather_data['humidity'].tolist(),   # 월별 평균 습도 리스트
        'wind_speed': weather_data['wind_speed'].tolist(), # 월별 평균 풍속 리스트
        'month': weather_data['month'].tolist()          # 월 리스트 (1~12월)
    }

    # 13. 템플릿에 연평균, 월평균, 계절별 및 날씨 데이터를 전달하여 렌더링
    return templates.TemplateResponse("dashboard.html", {
        "request": request,                          # FastAPI 요청 객체
        "pm25_data": pm25_data,                      # 연평균 PM2.5 데이터
        "pm10_data": pm10_data,                      # 연평균 PM10 데이터
        "pm25_monthly_data": pm25_monthly_data,      # 월평균 PM2.5 데이터
        "pm10_monthly_data": pm10_monthly_data,      # 월평균 PM10 데이터
        "pm25_season_data": pm25_season_data,        # 계절별 PM2.5 데이터
        "pm10_season_data": pm10_season_data,        # 계절별 PM10 데이터
        "weather_data": weather_data                 # 월별 습도 및 풍속 데이터
    })
