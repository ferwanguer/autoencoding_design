var text = document.getElementById("pp");
var text_2 = document.getElementById("p2");
const ctx = document.getElementById('myChart').getContext('2d');
const ctx_polar = document.getElementById('myChart_polar').getContext('2d')
// $("#pp")

let myChart = new Chart(ctx, {
  type: 'scatter',
  data: {
      labels: [-1,13],
      datasets: [{
          label: '# of Votes',
          data: [0,1],
          // backgroundColor: [
          //     'rgba(255, 99, 132, 0.2)',
          //     'rgba(54, 162, 235, 0.2)',
          //     'rgba(255, 206, 86, 0.2)',
          //     'rgba(75, 192, 192, 0.2)',
          //     'rgba(153, 102, 255, 0.2)',
          //     'rgba(255, 159, 64, 0.2)'
          // ],
          borderColor: [
              'rgba(255, 99, 132, 1)',
              
          ],
          borderWidth: 1
      }]
  },
  options: {
      scales: {
        
          y: {
              beginAtZero: true,
              min:-1.5,
              max: 1.5
          }
         
      }, responsive: false
  }
});

let myChart_p = new Chart(ctx_polar, {
    type: 'scatter',
    data: {
        labels: [-1,13],
        datasets: [{
            label: '# of Votes',
            data: [0,1],
            // backgroundColor: [
            //     'rgba(255, 99, 132, 0.2)',
            //     'rgba(54, 162, 235, 0.2)',
            //     'rgba(255, 206, 86, 0.2)',
            //     'rgba(75, 192, 192, 0.2)',
            //     'rgba(153, 102, 255, 0.2)',
            //     'rgba(255, 159, 64, 0.2)'
            // ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
          
            y: {
                beginAtZero: true,
                min:-1.5,
                max: 1.5
            }
           
        }, responsive: false
    }
  });

function sendinfo(value, value_2){
$.ajax({
    type: "POST",
    url: "/calculate",
    data: JSON.stringify({"valor" : value, "valor_2": value_2}),
    contentType: "application/json",
    dataType: 'json', 
    success: function(result){text.innerHTML=  result["x"]  ;
    text_2.innerHTML = result["y"];
    
    if(myChart !== null) {
      // Destruir para poder crear nuevamente
      myChart.destroy();}

  //  console.log(result)
   myChart = new Chart(ctx, {
    type: 'scatter',
    data: {
        labels: result["x_coordinate"],
        datasets: [{
            label: '# of Votes',
            data: result["y_coordinate"],
            // backgroundColor: [
            //     'rgba(255, 99, 132, 0.2)',
            //     'rgba(54, 162, 235, 0.2)',
            //     'rgba(255, 206, 86, 0.2)',
            //     'rgba(75, 192, 192, 0.2)',
            //     'rgba(153, 102, 255, 0.2)',
            //     'rgba(255, 159, 64, 0.2)'
            // ],
            borderColor: [
                'rgba(255, 99, 132, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        
        scales: {
          
            y: {
                beginAtZero: true,
                max: 1.5,
                min: -1.5
            }
           
        }, responsive: false, animation:false
    }})


    //  console.log(result)
    if(myChart_p !== null) {
        // Destruir para poder crear nuevamente
        myChart_p.destroy();} 
    
     myChart_p = new Chart(ctx_polar, {
        type: 'scatter',
        data: {
            labels: result["x_polar"],
            datasets: [{
                label: '# of Votes',
                data: result["y_polar"],
                // backgroundColor: [
                //     'rgba(255, 99, 132, 0.2)',
                //     'rgba(54, 162, 235, 0.2)',
                //     'rgba(255, 206, 86, 0.2)',
                //     'rgba(75, 192, 192, 0.2)',
                //     'rgba(153, 102, 255, 0.2)',
                //     'rgba(255, 159, 64, 0.2)'
                // ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
              
                y: {
                    beginAtZero: true,
                    min:-1.5,
                    max: 1.5
                }
               
            }, responsive: false, animation:false
        }
    });




















    }
});
}





