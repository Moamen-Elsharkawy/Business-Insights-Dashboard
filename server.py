from flask import Flask, jsonify, render_template
import sqlite3
from sqlite3 import Error
import pandas as pd
from sqlalchemy import create_engine, text

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

df = pd.read_csv("Company.csv")
connection = create_connection("sample.db")
df.to_sql("company", connection, if_exists='replace')
connection.close()

#db_url = 'sqlite:///sample.db'
#engine = create_engine(db_url, echo = True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-datapie')
def get_datachart(): #A pie chart to represent the average market share for each ProductCategory across all years.
    
    connection = create_connection("sample.db")
    db_url = 'sqlite:///sample.db'
    engine = create_engine(db_url, echo = True)
    data_df = pd.read_sql('SELECT ProductCategory, AVG(MarketShare) AS AverageMarketShare FROM company Where Year = (SELECT MAX(Year) FROM company) group by ProductCategory ORDER BY ProductCategory', engine)
    print(data_df)
    connection.close()

    df = pd.DataFrame(data_df)

    classes = df["ProductCategory"].value_counts().index
    data = []

    for i in range(len(classes)):
        data.append({ "class": classes[i], "value": int(df['AverageMarketShare'][i]) })
  #  print(data)

    return jsonify(data)

@app.route('/get-datascatter')
def get_datascatter(): #scatter

    connection = create_connection("sample.db")
    db_url = 'sqlite:///sample.db'
    engine = create_engine(db_url, echo = True)
    data_df = pd.read_sql('SELECT Branch, Employees AS NumberOfEmployees, SUM(Revenue)AS TotalRevenue FROM company WHERE Year = (SELECT MAX(Year) FROM company) Group By Branch', engine)
    #print(data_df)
    connection.close()

    df = pd.DataFrame(data_df)
    import random

    
    data = []

    
    used_colors = set()
    counter = 0
    
    for Branch in df['Branch'].unique():

        if Branch not in used_colors:

            new_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            
            data.append({'Branch': Branch, 'NumberOfEmployees': int(df['NumberOfEmployees'][counter]), 'TotalRevenue': int(df['TotalRevenue'][counter])  ,'Color': new_color, 'value': 14})
            counter += 1
            used_colors.add(new_color)
        

    #print(data)
    

    return jsonify(data)

@app.route('/get-dataclustered')
def get_dataclustered(): # clusterd bar chart

    connection = create_connection("sample.db")
    db_url = 'sqlite:///sample.db'
    engine = create_engine(db_url, echo = True)
    data_df = pd.read_sql('SELECT Branch, ProductCategory, SUM(Profit)AS TotalProfit FROM company WHERE Year = (SELECT MAX(Year) FROM company) GROUP BY Branch, ProductCategory ORDER BY Branch, ProductCategory ', engine)
    #print(data_df)
    connection.close()

    df = pd.DataFrame(data_df)
    
    temp = 0
    data = []
    for i in range(len(df['Branch'])):
        i = temp    
        data.append({ "Branch": str(df['Branch'][i]), "Consoles": float(df['TotalProfit'][i] ), "Laptops": float(df['TotalProfit'][i+1] ), "Mobile Devices": float(df['TotalProfit'][i+2] )  })
        temp = i + 3
        i = i + 3
        if i == (len(df['Branch']) or len(df['Branch']) - 1 or len(df['Branch']) - 2  ):
            break
    #print(data)
    
    
    return jsonify(data)

@app.route('/get-databar')
def get_dataline(): # bar

    connection = create_connection("sample.db")
    db_url = 'sqlite:///sample.db'
    engine = create_engine(db_url, echo = True)
    data_df = pd.read_sql('SELECT Branch, SUM(TotalCustomers) as TotalCustomersLastYear FROM company Group By Branch;', engine)
    #print(data_df)
    connection.close()

    df = pd.DataFrame(data_df)

    
    data = []

    for i in range(len(df['Branch'])):
        data.append({ 'Branch': str(df["Branch"][i]), 'TotalCustomersLastYear': int(df['TotalCustomersLastYear'][i]) })

    
    #print(data)

 

    return jsonify(data)


@app.route('/get-datatable')
def get_datatable():
    return jsonify(df[0:5].to_html())

if __name__ == '__main__':
    app.run(debug=True)

