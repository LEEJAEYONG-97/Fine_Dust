document.addEventListener("DOMContentLoaded", function() {
    const chartData = document.getElementById('chart-data');

    // Weather data parsing
    const weatherData = JSON.parse(chartData.dataset.weather);
    const weatherCtx = document.getElementById('weatherChart').getContext('2d');
    
    new Chart(weatherCtx, {
        type: 'bar',  // 기본 차트는 바 차트로 습도를 표시
        data: {
            labels: weatherData.month.map(month => `${month}월`),  // x축 라벨에 '월'을 추가
            datasets: [
                {
                    label: '평균 습도(%)',
                    data: weatherData.humidity,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',  // 습도는 파란색 막대로 표시
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    yAxisID: 'y'  // 왼쪽 y축
                },
                {
                    label: '평균 풍속(m/s)',
                    data: weatherData.wind_speed,
                    type: 'line',  // 풍속은 선 그래프로 표시
                    borderColor: 'rgba(255, 159, 64, 1)',
                    fill: false,
                    yAxisID: 'y1'  // 오른쪽 y축
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: '한국 월평균 습도 및 풍속 차트'
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display: false  // x축 그리드 삭제
                    },
                    ticks: {
                        callback: function(value) {
                            return `${value}`;  // x축 라벨을 'x월' 형식으로 변경
                        }
                    }
                }],
                yAxes: [
                    {
                        id: 'y',
                        type: 'linear',
                        position: 'left',
                        gridLines: {
                            display: false  // y축 왼쪽 그리드 삭제
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '습도 (%)'
                        }
                    },
                    {
                        id: 'y1',
                        type: 'linear',
                        position: 'right',
                        gridLines: {
                            display: false  // y축 오른쪽 그리드 삭제
                        },
                        ticks: {
                            min: 2.0,  // y축의 최소값을 2.0으로 설정
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '풍속 (m/s)'
                        }
                    }
                ]
            }
        }
    });
});
