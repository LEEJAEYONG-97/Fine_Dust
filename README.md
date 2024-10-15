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

1. **Korean BERT Model**: A pre-trained language model that demonstrates very strong performance in the field of Natural Language Processing (NLP). Developed by Google, it excels in understanding context.
2. **LDA Model**: Models each topic as a probability distribution of words. It is used to uncover hidden topics in text data. Specific topics are understood as sets of words that have a high probability of occurrence together.
It employs non-parametric Bayesian methods, such as Gibbs sampling, to infer topics. The process involves iterative sampling while considering the number of topics and words.



# Analysis of Tourist Ratings and Reviews

Most well-known tourist attractions have high ratings.



# Review Length Distribution

Many reviews are under 50 characters and are evenly distributed.




# Word Frequency Analysis

The analysis of reviews showed that "child" had the highest frequency.



# Sentiment Analysis

Using the Korean BERT model, we found that there are many positive reviews.

![image6](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EA%B0%90%EC%84%B1%EB%B6%84%EC%84%9D.png)

# Topic Modeling

When using the LDA model, "child," "time," and "visit" were identified as significant topics.

![image7](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%A3%BC%EC%A0%9C%20%ED%86%A0%ED%94%BD.png)

# Wordcolud

![image9](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png)

# Map

![image8](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%A7%80%EB%8F%84.png)

# WebService
![image10](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%9B%B9%EA%B5%AC%ED%98%84.png)
![image11](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%9B%B9%EA%B5%AC%ED%98%843.png)
![image12](https://github.com/LEEJAEYONG-97/portfolio/blob/5f895857ba9189f1b1c950e016cf4d3267e19425/app/static/assets/img/%EC%9B%B9%EA%B5%AC%ED%98%844.png)
