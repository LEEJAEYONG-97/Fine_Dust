![image](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/main2.png)

# Time Series Model-Based Prediction of Fine Dust from China to Korea
The goal is to analyze the impact of China's air quality, including fine dust, on Korea's air environment, and to provide a web service for predicting air quality in Korea based on this analysis.

![image alt](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/main.png)

# Data Collection

* Korean Air Quality Data: Date, PM2.5, PM10, O3, NO2, SO2, CO
* China Air Quality Data: Date, PM2.5, PM10, O3, NO2, SO2, CO
* Korean weather data: Date, humidity, wind speed


* PM2.5: Fine dust with a diameter of 2.5 micrometers or less.
* PM10: Fine dust with a diameter of 10 micrometers or less.
* O3 (Ozone): Triatomic oxygen that occurs in the atmosphere.
* NO2 (Nitrogen Dioxide): A nitrogen oxide produced from industrial processes.
* SO2 (Sulfur Dioxide): A cause of acid rain in the atmosphere.
* CO (Carbon Monoxide): A colorless, odorless gas produced from incomplete combustion.

Regions:

* China: Beijing, Shanghai, Tianjin, Gobi Desert, and 20 other cities.
* Korea: Seoul, Busan, Daegu, Daejeon, Gwangju, Ulsan, and 20 other cities.

Source: AQICN , Weather Data Open Portal
Data common collection period: January 2013 to September 2024

# Data Preprocessing Steps

1. **Date sorting**
2. **Type conversion**
3. **Missing value removal**

# Correlation analysis

Correlation analysis between Chinese weather factors and Korean weather factors
A result of 0.4 or higher indicates a correlation, leading to the final variable selection


![image2](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/heatmap2.png)


Humidity shows a negative correlation



![image3](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/heatmap.png)


# EDA
**Exploratory Data Analysis (EDA)**: Comparison of annual average, monthly average, and seasonal fine dust levels between China and Korea, along with visualization of monthly average humidity and wind speed in Korea. using Pandas, Seaborn, and Matplotlib.

![image4](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/eda.png)
![image5](https://github.com/LEEJAEYONG-97/portfolio/blob/341803756a1e4620a4ff964c1f0b7a25d9f3b212/app/static/assets/img/eda2.png)


It can be observed that fine dust levels are high in winter, with strong wind speeds and low humidity.

# Models

### LSTM (Long Short-Term Memory)
LSTM is a type of recurrent neural network (RNN) designed to model time series data and sequences. It addresses the problem of vanishing gradients in standard RNNs by using memory cells that can maintain information over long periods. This makes LSTM particularly effective for tasks like speech recognition, language modeling, and time series forecasting, where past information is crucial for making predictions.

### ARIMA (AutoRegressive Integrated Moving Average)
ARIMA is a popular statistical model used for forecasting time series data. It combines three components: 
- **AutoRegressive (AR)**: uses the relationship between an observation and a number of lagged observations.
- **Integrated (I)**: involves differencing the data to make it stationary (constant mean and variance).
- **Moving Average (MA)**: uses the dependency between an observation and a residual error from a moving average model.

ARIMA is well-suited for univariate time series forecasting, particularly when the data shows trends or seasonality.

### Kalman Filter
The Kalman filter is an algorithm that uses a series of measurements observed over time, containing statistical noise and other inaccuracies, to estimate unknown variables. It operates in a two-step process: 
1. **Prediction**: Estimates the current state based on the previous state.
2. **Update**: Adjusts the estimates based on the new measurement.

Kalman filters are widely used in control systems, navigation, and time series analysis, providing a way to infer the hidden state of a system over time.

![image6](https://github.com/LEEJAEYONG-97/portfolio/blob/8168128b106a7c676d7b7f06dd6ac93d990732a8/app/static/assets/img/predict.png)

# Model Evaluation
Performance comparison of the LSTM multivariate time series model
||mse|R^2SCORE|
|:---:|:---:|:---:|
|LSTM|0.009|0.437|
Performance comparison of the ARIMA time series model
||mse|R^2SCORE|
|:---:|:---:|:---:|
|pm25|109.006|-133.524|
|pm10|12.975|-4.308|
Performance comparison of the Kalman Filter model
||mse|R^2SCORE|
|:---:|:---:|:---:|
|pm25|63.4558|0.9128|
|pm10|31.0998|0.9033|
Comparison of MSE and R² Score among the three models:

- MSE: LSTM > Kalman Filter > ARIMA  
- R² Score: Kalman Filter > LSTM > ARIMA  

Although LSTM has a higher MSE, it is best suited for multivariate factors and complex models, demonstrating the best overall performance.


# Web structure

![image7](https://github.com/LEEJAEYONG-97/portfolio/blob/d1cd4231fc5d8e9fc7edc10bd7ab1b8659a3d6e2/app/static/assets/img/web.png)

# WebService
![image10](https://github.com/LEEJAEYONG-97/portfolio/blob/d1cd4231fc5d8e9fc7edc10bd7ab1b8659a3d6e2/app/static/assets/img/web2.png)
![image11](https://github.com/LEEJAEYONG-97/portfolio/blob/d1cd4231fc5d8e9fc7edc10bd7ab1b8659a3d6e2/app/static/assets/img/web3.png)

