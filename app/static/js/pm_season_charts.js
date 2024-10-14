document.addEventListener("DOMContentLoaded", function() {
    const chartData = document.getElementById('chart-data');

    // PM2.5 계절별 데이터 파싱
    const pm25SeasonData = JSON.parse(chartData.dataset.pm25Season);
    const pm25SeasonCtx = document.getElementById('pm25SeasonChart').getContext('2d');
    new Chart(pm25SeasonCtx, {
        type: 'bar',  // 막대형 차트 사용
        data: {
            labels: pm25SeasonData.season,  // 계절 이름 (봄, 여름, 가을, 겨울)
            datasets: [
                {
                    label: '한국 PM2.5',
                    data: pm25SeasonData.korea,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',  // 한국 데이터 막대 색상
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: '중국 PM2.5',
                    data: pm25SeasonData.china,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',  // 중국 데이터 막대 색상
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM2.5 계절별 평균 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: true
                    },
                    ticks: {
                        beginAtZero: true  // y축 값이 0에서 시작
                    }
                }]
            }
        }
    });

    // PM10 계절별 데이터 파싱
    const pm10SeasonData = JSON.parse(chartData.dataset.pm10Season);
    const pm10SeasonCtx = document.getElementById('pm10SeasonChart').getContext('2d');
    new Chart(pm10SeasonCtx, {
        type: 'bar',  // 막대형 차트 사용
        data: {
            labels: pm10SeasonData.season,  // 계절 이름 (봄, 여름, 가을, 겨울)
            datasets: [
                {
                    label: '한국 PM10',
                    data: pm10SeasonData.korea,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',  // 한국 데이터 막대 색상
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: '중국 PM10',
                    data: pm10SeasonData.china,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',  // 중국 데이터 막대 색상
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM10 계절별 평균 비교 (한국 vs 중국)'
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: true
                    },
                    ticks: {
                        beginAtZero: true  // y축 값이 0에서 시작
                    }
                }]
            }
        }
    });
});
