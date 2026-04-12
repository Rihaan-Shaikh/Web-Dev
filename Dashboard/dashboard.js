/* globals Chart:false */

(() => {
  'use strict'

  // Graphs
    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
            datasets: [{
                label: 'Sepal Length (cm)',
                data: [5.1,4.9,4.7,4.6,5.0,5.4,4.6,5.0,4.4,4.9,5.4,4.8,4.8,4.3,5.8],
                backgroundColor: '#3245ff'
            }]
        },
        options: {
            plugins: {
                legend: { display: true }
            }
        }
    })
})()
