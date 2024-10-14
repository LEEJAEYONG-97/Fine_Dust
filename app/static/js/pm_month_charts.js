document.addEventListener("DOMContentLoaded", function() {
    const chartData = document.getElementById('chart-data');

    // PM2.5 월평균 데이터 파싱
    const pm25MonthlyData = JSON.parse(chartData.dataset.pm25Monthly);
    const pm25MonthlyCtx = document.getElementById('pm25MonthlyChart').getContext('2d');
    new Chart(pm25MonthlyCtx, {
        type: 'line',
        data: {
            labels: pm25MonthlyData.month,  // 월을 x축 라벨로 사용
            datasets: [
                {
                    label: '한국 PM2.5',
                    data: pm25MonthlyData.korea,
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: '중국 PM2.5',
                    data: pm25MonthlyData.china,
                    borderColor: 'red',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM2.5 월평균 데이터 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    type: 'category',  // 월을 카테고리로 설정
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        callback: function(value) {
                            return value + '월';  // 월을 그대로 사용
                        }
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: false
                    }
                }]
            }
        }
    });

    // PM10 월평균 데이터 파싱
    const pm10MonthlyData = JSON.parse(chartData.dataset.pm10Monthly);
    const pm10MonthlyCtx = document.getElementById('pm10MonthlyChart').getContext('2d');
    new Chart(pm10MonthlyCtx, {
        type: 'line',
        data: {
            labels: pm10MonthlyData.month,  // 월을 x축 라벨로 사용
            datasets: [
                {
                    label: '한국 PM10',
                    data: pm10MonthlyData.korea,
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: '중국 PM10',
                    data: pm10MonthlyData.china,
                    borderColor: 'red',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM10 월평균 데이터 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    type: 'category',  // 월을 카테고리로 설정
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        callback: function(value) {
                            return value + '월';  // 월을 그대로 사용
                        }
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: false
                    }
                }]
            }
        }
    });
});
