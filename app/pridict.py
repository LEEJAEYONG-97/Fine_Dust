import requests
import pandas as pd

# FastAPI 서버 URL
url = 'http://127.0.0.1:8000/predict/'

# CSV 파일 경로
file_path = 'C:/Users/M/jupyter_Work/Finddust/predict_df.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 데이터 필터링: 필요한 열만 포함된 데이터프레임 생성
df_filtered = df[['date', 'pm25_china_df', 'pm10_china_df', 'o3_china_df', 'no2_china_df', 
                  'so2_china_df', 'co_china_df', 'Wind Speed(m/s)', 'Humidity(%)']]
df_filtered.rename(columns={
    'Wind Speed(m/s)': 'wind_speed_mps',
    'Humidity(%)': 'humidity_percent'
}, inplace=True)

# 예측 수행 및 결과 출력
for _, row in df_filtered.iterrows():
    data = {
        'date': row['date'],
        'pm25_china_df': row['pm25_china_df'],
        'pm10_china_df': row['pm10_china_df'],
        'o3_china_df': row['o3_china_df'],
        'no2_china_df': row['no2_china_df'],
        'so2_china_df': row['so2_china_df'],
        'co_china_df': row['co_china_df'],
        'wind_speed_mps': row['wind_speed_mps'],
        'humidity_percent': row['humidity_percent']
    }

    # form-encoded 형식으로 요청 보내기
    response = requests.post(url, data=data)
    if response.status_code == 200:
        result = response.json()
        print(f"Input Data: {data}")
        print(f"Prediction: {result}")
    else:
        print(f"Failed to get a valid response. Status code: {response.status_code}")
        print(f"Response: {response.text}")
    print("-" * 50)
