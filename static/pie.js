function fetchDataAndUpdatepie() {
    fetch('/get-datapie')
        .then(response => response.json())
        .then(data => {
            updatepie(data);
        })
        .catch(error => console.error('Error:', error));
}
function updatepie(data_df) {

  am5.ready(function() {
        // Create root and chart
    var root = am5.Root.new("pie");
    var chart = root.container.children.push( 
      am5percent.PieChart.new(root, {
        layout: root.verticalHorizontal
      }) 
    );

    // Define data
    var data = [{
      country: "France",
      sales: 100000
    }, {
      country: "Spain",
      sales: 160000
    }, {
      country: "United Kingdom",
      sales: 80000
    }];

    // Create series
    var series = chart.series.push(
      am5percent.PieSeries.new(root, {
        name: "Series",
        valueField: "value",
        categoryField: "class"
      })
    );
    series.data.setAll(data_df);
    console.log(data_df);

    // Add legend
    var legend = chart.children.push(am5.Legend.new(root, {
      centerX: am5.percent(50),
      x: am5.percent(50),
      layout: root.horizontalLayout
    }));

    legend.data.setAll(series.dataItems);

    




  


    
   

  }); // end am5.ready()
}
document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdatepie()
});
 