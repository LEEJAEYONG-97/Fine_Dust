document.addEventListener("DOMContentLoaded", function() {
    const chartData = document.getElementById('chart-data');

    // PM2.5 데이터 파싱
    const pm25Data = JSON.parse(chartData.dataset.pm25);
    const pm25Ctx = document.getElementById('pm25Chart').getContext('2d');
    new Chart(pm25Ctx, {
        type: 'line',
        data: {
            labels: pm25Data.year,  // 연도를 x축 라벨로 사용
            datasets: [
                {
                    label: '한국 PM2.5',
                    data: pm25Data.korea,
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: '중국 PM2.5',
                    data: pm25Data.china,
                    borderColor: 'red',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM2.5 연평균 데이터 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    type: 'category',  // 연도를 카테고리로 설정
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        callback: function(value) {
                            return value;  // 연도 값을 그대로 사용
                        }
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

    // PM10 데이터 파싱
    const pm10Data = JSON.parse(chartData.dataset.pm10);
    const pm10Ctx = document.getElementById('pm10Chart').getContext('2d');
    new Chart(pm10Ctx, {
        type: 'line',
        data: {
            labels: pm10Data.year,  // 연도를 x축 라벨로 사용
            datasets: [
                {
                    label: '한국 PM10',
                    data: pm10Data.korea,
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: '중국 PM10',
                    data: pm10Data.china,
                    borderColor: 'red',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM10 연평균 데이터 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    type: 'category',  // 연도를 카테고리로 설정
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        callback: function(value) {
                            return value;  // 연도 값을 그대로 사용
                        }
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});
