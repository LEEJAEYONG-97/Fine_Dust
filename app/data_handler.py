import pandas as pd

def load_yearly_avg_data(kor_file, cha_file):
    # 한국 데이터 로드 및 처리
    kor_data = pd.read_csv(kor_file)
    kor_data['date'] = pd.to_datetime(kor_data['date'], errors='coerce')
    kor_data['year'] = kor_data['date'].dt.year

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    kor_data['pm25'] = pd.to_numeric(kor_data['pm25'], errors='coerce')
    kor_data['pm10'] = pd.to_numeric(kor_data['pm10'], errors='coerce')

    # 'pm25', 'pm10' 컬럼의 결측치를 0으로 처리
    kor_data[['pm25', 'pm10']] = kor_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    kor_data_filtered = kor_data[(kor_data['year'] >= 2015) & (kor_data['year'] <= 2023)]

    # 각 날짜별로 PM2.5, PM10의 평균을 계산
    kor_daily_avg = kor_data_filtered.groupby('date')[['pm25', 'pm10']].mean().reset_index(drop=True)

    # 연도별로 그룹화하여 연평균 계산 (year로 그룹화, date는 없음)
    kor_yearly_avg = kor_data_filtered.groupby('year')[['pm25', 'pm10']].mean().reset_index()

    # 중국 데이터 로드 및 처리
    cha_data = pd.read_csv(cha_file)
    cha_data['date'] = pd.to_datetime(cha_data['date'], errors='coerce')
    cha_data['year'] = cha_data['date'].dt.year

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    cha_data['pm25'] = pd.to_numeric(cha_data['pm25'], errors='coerce')
    cha_data['pm10'] = pd.to_numeric(cha_data['pm10'], errors='coerce')

    # 'pm25', 'pm10' 컬럼의 결측치를 0으로 처리
    cha_data[['pm25', 'pm10']] = cha_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    cha_data_filtered = cha_data[(cha_data['year'] >= 2015) & (cha_data['year'] <= 2023)]

    # 각 날짜별로 PM2.5, PM10의 평균을 계산
    cha_daily_avg = cha_data_filtered.groupby('date')[['pm25', 'pm10']].mean().reset_index(drop=True)

    # 연도별로 그룹화하여 연평균 계산
    cha_yearly_avg = cha_data_filtered.groupby('year')[['pm25', 'pm10']].mean().reset_index()

    return kor_yearly_avg, cha_yearly_avg

def load_monthly_avg_data(kor_file, cha_file):
    # 한국 데이터 로드 및 처리
    kor_data = pd.read_csv(kor_file)
    kor_data['date'] = pd.to_datetime(kor_data['date'], errors='coerce')
    kor_data['year'] = kor_data['date'].dt.year  # 연도 추출
    kor_data['month'] = kor_data['date'].dt.month  # 월만 추출

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    kor_data['pm25'] = pd.to_numeric(kor_data['pm25'], errors='coerce')
    kor_data['pm10'] = pd.to_numeric(kor_data['pm10'], errors='coerce')
    
    # 'pm25', 'pm10' 컬럼의 결측치를 0으로 처리
    kor_data[['pm25', 'pm10']] = kor_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    kor_data_filtered = kor_data[(kor_data['year'] >= 2015) & (kor_data['year'] <= 2023)]

    # 월별 PM2.5, PM10의 평균을 계산
    kor_monthly_avg = kor_data_filtered.groupby('month')[['pm25', 'pm10']].mean().reset_index()

    # 중국 데이터 로드 및 처리
    cha_data = pd.read_csv(cha_file)
    cha_data['date'] = pd.to_datetime(cha_data['date'], errors='coerce')
    cha_data['year'] = cha_data['date'].dt.year  # 연도 추출
    cha_data['month'] = cha_data['date'].dt.month  # 월만 추출

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    cha_data['pm25'] = pd.to_numeric(cha_data['pm25'], errors='coerce')
    cha_data['pm10'] = pd.to_numeric(cha_data['pm10'], errors='coerce')
    
    # 'pm25', 'pm10' 컬럼의 결측치를 0으로 처리
    cha_data[['pm25', 'pm10']] = cha_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    cha_data_filtered = cha_data[(cha_data['year'] >= 2015) & (cha_data['year'] <= 2023)]

    # 월별 PM2.5, PM10의 평균을 계산
    cha_monthly_avg = cha_data_filtered.groupby('month')[['pm25', 'pm10']].mean().reset_index()

    return kor_monthly_avg, cha_monthly_avg

def get_season(month):
    """월을 기반으로 계절을 반환하는 함수"""
    if month in [12, 1, 2]:
        return '겨울'
    elif month in [3, 4, 5]:
        return '봄'
    elif month in [6, 7, 8]:
        return '여름'
    elif month in [9, 10, 11]:
        return '가을'

def load_seasonal_avg_data(kor_file, cha_file):
    # 한국 데이터 로드 및 처리
    kor_data = pd.read_csv(kor_file)
    kor_data['date'] = pd.to_datetime(kor_data['date'], errors='coerce')
    kor_data['year'] = kor_data['date'].dt.year
    kor_data['month'] = kor_data['date'].dt.month
    kor_data['season'] = kor_data['month'].apply(get_season)

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    kor_data['pm25'] = pd.to_numeric(kor_data['pm25'], errors='coerce')
    kor_data['pm10'] = pd.to_numeric(kor_data['pm10'], errors='coerce')

    # 결측치를 0으로 처리
    kor_data[['pm25', 'pm10']] = kor_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    kor_data_filtered = kor_data[(kor_data['year'] >= 2015) & (kor_data['year'] <= 2023)]

    # 계절별 PM2.5, PM10의 평균을 계산
    kor_seasonal_avg = kor_data_filtered.groupby('season')[['pm25', 'pm10']].mean().reset_index()

    # 중국 데이터 로드 및 처리
    cha_data = pd.read_csv(cha_file)
    cha_data['date'] = pd.to_datetime(cha_data['date'], errors='coerce')
    cha_data['year'] = cha_data['date'].dt.year
    cha_data['month'] = cha_data['date'].dt.month
    cha_data['season'] = cha_data['month'].apply(get_season)

    # pm25, pm10 컬럼을 숫자로 강제 변환 (변환 불가 값은 NaN 처리)
    cha_data['pm25'] = pd.to_numeric(cha_data['pm25'], errors='coerce')
    cha_data['pm10'] = pd.to_numeric(cha_data['pm10'], errors='coerce')

    # 결측치를 0으로 처리
    cha_data[['pm25', 'pm10']] = cha_data[['pm25', 'pm10']].fillna(0)

    # 2015년 ~ 2023년 데이터 필터링
    cha_data_filtered = cha_data[(cha_data['year'] >= 2015) & (cha_data['year'] <= 2023)]

    # 계절별 PM2.5, PM10의 평균을 계산
    cha_seasonal_avg = cha_data_filtered.groupby('season')[['pm25', 'pm10']].mean().reset_index()

    return kor_seasonal_avg, cha_seasonal_avg

def load_monthly_weather(file):
    """
    한국 날씨 데이터를 로드하여 일별 평균 계산 후 월별 평균으로 변환하는 함수
    :param file: csv 파일 경로
    :return: 월별 습도 및 풍속 평균 데이터 (1월 ~ 12월)
    """
    # 인코딩을 'ISO-8859-1' 또는 'EUC-KR'로 시도
    try:
        data = pd.read_csv(file, encoding='utf-8')  # 기본 UTF-8 시도
    except UnicodeDecodeError:
        data = pd.read_csv(file, encoding='EUC-KR')  # 다른 인코딩 시도
    
    # 날짜 형식으로 변환
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    
    # 연도와 월 추출
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    
    # 습도와 풍속 데이터를 숫자로 변환 (NaN 처리 포함)
    data['humidity'] = pd.to_numeric(data['humidity'], errors='coerce').fillna(0)
    data['wind_speed'] = pd.to_numeric(data['wind_speed'], errors='coerce').fillna(0)
    
    # 2015년 ~ 2023년 데이터 필터링
    filtered_data = data[(data['year'] >= 2015) & (data['year'] <= 2023)]
    
    # 중복된 날짜에 대한 일평균 계산 (도시별 데이터를 종합하여 일평균 계산)
    daily_avg = filtered_data.groupby('date')[['humidity', 'wind_speed']].mean().reset_index()
    
    # 월별 습도 및 풍속 평균 계산
    daily_avg['month'] = daily_avg['date'].dt.month  # 월만 추출
    monthly_avg = daily_avg.groupby('month')[['humidity', 'wind_speed']].mean().reset_index()

    return monthly_avg
