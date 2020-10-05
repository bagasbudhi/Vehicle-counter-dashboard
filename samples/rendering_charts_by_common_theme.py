from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Overlapped Bar 2D and column 2d chart where data is passed as JSON string format.
# These charts are rendering with a common theme.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

  datasources = "/static/data/data2.json" 
  data2 = "/static/data/data3.json"
    # Create an object for the overlappedbar2d chart using the FusionCharts class constructor
  overlappedcolumn2d = FusionCharts("overlappedcolumn2d", "ex1" , "700", "500", "chart-1","jsonurl",datasources)
        # The data is passed as a string in the `dataSource` as parameter.
    

         # import json

          #file_json =open('/static/data/data1.json')
          #data =json.loads(file_json)
          #print data

         
       
    # Create an object for the column2d chart using the FusionCharts class constructor
  column2d = FusionCharts("column2d", "ex2" , "700", "500", "chart-2", "jsonurl",data2) 
        # The data is passed as a string in the `dataSource` as parameter.)
 
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'chart-theme.html', {'output1' : overlappedcolumn2d.render(), 'output2' : column2d.render(), 'chartTitle': 'Chart Themes'}) 

#