document.addEventListener("DOMContentLoaded", function() {
    const chartData = document.getElementById('chart-data');

    // PM2.5 초과 일수 데이터 파싱
    const pm25ExceedanceData = JSON.parse(chartData.dataset.pm25Exceedance);
    const pm25Years = Object.keys(pm25ExceedanceData);
    const pm25Days = Object.values(pm25ExceedanceData);
    const pm25Ctx = document.getElementById('pm25ExceedanceChart').getContext('2d');
    new Chart(pm25Ctx, {
        type: 'bar',
        data: {
            labels: pm25Years,
            datasets: [{
                label: 'Days Exceeding PM2.5 Guideline (35 μg/m³)',
                data: pm25Days,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM2.5 Exceedance Days per Year'
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display: false
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

    // PM10 초과 일수 데이터 파싱
    const pm10ExceedanceData = JSON.parse(chartData.dataset.pm10Exceedance);
    const pm10Years = Object.keys(pm10ExceedanceData);
    const pm10Days = Object.values(pm10ExceedanceData);
    const pm10Ctx = document.getElementById('pm10ExceedanceChart').getContext('2d');
    new Chart(pm10Ctx, {
        type: 'bar',
        data: {
            labels: pm10Years,
            datasets: [{
                label: 'Days Exceeding PM10 Guideline (100 μg/m³)',
                data: pm10Days,
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'PM10 Exceedance Days per Year'
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display: false
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
