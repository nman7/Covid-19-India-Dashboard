# Covid-19-India-Dashboard
It is a website developed using Flask ,which includes daily updates of Covid-19 cases and has various functionality for getting insights of various Indian states affected by this pandemic.(https://naumanspare.pythonanywhere.com/)



# Code Overview.

  static:-includes images used in website.
  
  templates:-incudes html files used in website.
  
  main.py :- it is main python file.
  
  
  
  
1.  run "main.py" after that once server is running you will be accesing "/" route which invokes "home()" which includes:-

    makejson():- request covid data from "https://api.rootnet.in/covid19-in/stats/latest" and store it in json format "data_file.json".
    
    makecsv():- converts data_file.json  to csv  as "data_file.csv".

    read data_file.csv and pass access specific columns , store it as "cases_list" and dump it as json format to "home.html". 

    ("template" variable includes html code written using cases_list every time you access / route and stored it as "overall.html")
    
    
    
    
2. /geo:- dumps json data to maps.html and render it.

   /donut:- dumps json data to donut.html and render it.
   
   /recoverd:-dumps json data to maps.html and render it.
   
   /overall:-render overall.html(html code stored in "template" which was written on accessing "/") .
   
   
   
   
 3. map.html:- Indian map chart.
 
    donut.html:- Donut chart (used in recovered and  fatality chart).
    
    overall.html:-Table format for displaying data. 
