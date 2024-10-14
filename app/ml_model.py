import pandas as pd
import joblib
import numpy as np
from tensorflow.keras.models import load_model

# 모델 및 스케일러 로드
model = load_model('app/model/lstm_model.keras')
scaler_X = joblib.load('app/model/scaler_X.pkl')
scaler_y = joblib.load('app/model/scaler_y.pkl')

# 예측을 위한 전처리 함수
def preprocess_data(pm25, pm10, o3, no2, so2, co, wind_speed, humidity):
    data = pd.DataFrame([{
        'pm25_china_df': pm25,
        'pm10_china_df': pm10,
        'o3_china_df': o3,
        'no2_china_df': no2,
        'so2_china_df': so2,
        'co_china_df': co,
        'Wind Speed(m/s)': wind_speed,
        'Humidity(%)': humidity
    }])

    # 필요한 입력 피처만 선택하여 스케일링
    input_features = ['pm25_china_df', 'pm10_china_df', 'o3_china_df', 'no2_china_df', 'so2_china_df', 'co_china_df', 'Wind Speed(m/s)', 'Humidity(%)']
    data = data[input_features]

    # 데이터 정규화
    data_scaled = scaler_X.transform(data)
    return data_scaled

# 예측 함수
def make_prediction(input_data):
    # 입력 데이터 전처리 및 예측
    SEQ_LENGTH = 1  # 시퀀스 길이
    input_data_scaled = input_data.reshape(1, SEQ_LENGTH, -1)

    # 모델을 통한 예측
    prediction_scaled = model.predict(input_data_scaled)

    # 예측값을 다시 스케일링 해제
    prediction = scaler_y.inverse_transform(prediction_scaled)

    # 예측 결과가 0 미만이면 0으로 처리
    prediction = np.maximum(prediction, 0)

    return prediction.flatten().tolist()  # 리스트 형태로 반환
