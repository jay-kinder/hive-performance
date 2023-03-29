function wellnessLineChart(dates, scores){
    console.log(dates)
    Highcharts.chart('container', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Wellness Score Per Day'
        },
        xAxis: {
            categories:dates,
            crosshair: true,
            title: {
                text: 'Date Submitted'
            }
        },
        yAxis: {
            min: 0,
            max: 40,
            title: {
                text: 'Wellness Score (max 40)'
            }
        },
        plotOptions: {
            series: {
                color: '#d69f15'
            }
        },
        series: [{
            name: 'Wellness Score',
            data: scores
        }]
    });
}