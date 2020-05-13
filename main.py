from flask import Flask,render_template
import requests 
import json
import csv 

def makejson():   
    URL = "https://api.rootnet.in/covid19-in/stats/latest"
    r = requests.get(url = URL)
    f = r.json()
    newf=f['data']
    with open("data_file.json", "w") as write_file:
        json.dump(newf, write_file)


def makecsv():
    with open('data_file.json') as json_file: 
        data = json.load(json_file) 
    regional_data = data['regional'] 
    # now we will open a file for writing 
    data_file = open('data_file.csv', 'w') 
    # create the csv writer object 
    csv_writer = csv.writer(data_file) 
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0
    
    for emp in regional_data: 
        if count == 0: 
    
            # Writing headers of CSV file 
            header = emp.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(emp.values()) 
    
    data_file.close()




app = Flask(__name__)



@app.route('/donut')
def donut():
    import pandas as pd
    covid = pd.read_csv('data_file.csv')
    cases = covid[['loc','deaths']]
    cases.at[29,'loc']= 'Uttaranchal'
    cases.at[23,'loc']= 'Orissa'
    cases_list =[]
    cases_list.append(['State','Deaths'])
    cases_list.extend(cases.values.tolist())
    return render_template('donut.html', datas=json.dumps(cases_list))


@app.route('/recovered')
def recovered():
    import pandas as pd
    covid = pd.read_csv('data_file.csv')
    cases = covid[['loc','discharged']]
    cases.at[29,'loc']= 'Uttaranchal'
    cases.at[23,'loc']= 'Orissa'
    cases_list =[]
    cases_list.append(['State','Patients Recovered'])
    cases_list.extend(cases.values.tolist())
    return render_template('recovered.html', datas=json.dumps(cases_list))


@app.route('/')
def home():
    makejson()
    makecsv()
    URL = "https://api.rootnet.in/covid19-in/stats/latest"
    r = requests.get(url = URL)
    f = r.json()
    ff=f['data']
    newff = ff['summary']
    t  = newff['total']
    d = newff['deaths']

    import pandas as pd
    covid = pd.read_csv('data_file.csv')
    cases = covid[['loc','totalConfirmed','deaths','discharged']]
    cases.at[29,'loc']= 'Uttaranchal'
    cases.at[23,'loc']= 'Orissa'
    cases_list =[]
    cases_list.append(['State','Total Cases','deaths','discharged'])
    cases_list.extend(cases.values.tolist())
    
    from mako.template import Template
    rows = cases_list
    template = """
        <html>
        <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <link rel="icon" type="image/png" sizes="32x32" href="static/h.png">
                        <!-- Image and text -->
            <nav class="navbar navbar-light bg-light">
                <a class="navbar-brand" href="/">
                <img src="/static/h.png" width="30" height="30" class="d-inline-block align-top" alt="">
                Daily Covid-19 Counter
                </a>
            </nav>
                    
                    <head>
            <body>
                <table class="table table-dark">
                     % for row in rows:
                     <tr>
                          % for cell in row:
                          <td>${cell}</td>
                          % endfor
                     </tr>
                     % endfor
                </table>
            </body>
        </html>"""
    jio = Template(template).render(rows=rows)

    Html_file= open("templates/overall.html","w")
    Html_file.write(jio)
    Html_file.close()


    return render_template('home.html',t=t,d=d,datas=json.dumps(cases_list))




@app.route('/overall')
def overall():
    return render_template('overall.html')













@app.route('/geo')
def map():
    import pandas as pd
    covid = pd.read_csv('data_file.csv')
    cases = covid[['loc','totalConfirmed']]
    cases.at[29,'loc']= 'Uttaranchal'
    cases.at[23,'loc']= 'Orissa'
    cases_list =[]
    cases_list.append(['State','Total Cases'])
    cases_list.extend(cases.values.tolist())
    return render_template('maps.html', datas=json.dumps(cases_list))


app.run(debug=True)