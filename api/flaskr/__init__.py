import os
from flask import Flask, render_template, request
from .data import *
import requests

url = "https://api.countrystatecity.in/v1/countries/"

headers = {
  'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
}
response = requests.request("GET", url, headers=headers)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
        return render_template('base.html', data=data)

    @app.route('/<Data>')
    def world(Data):
        placeholder = []
        for x in data['card']:
            placeholder.append(x['option'])
        if Data == 'World_Map':
            return render_template('world.html', data=data)
        elif Data == 'Search_Country':
            return render_template('search.html', data=data)
        elif Data == 'Country_List':
            return render_template('countrylist.html', data=data)
        else:
            return render_template('error.html', data=data)


    @app.route('/WorldMap/<country>', methods=['GET'])
    def output(country):
        contry = []
        for x in response:
            contry.append(x)
        if country in contry:
            countrydata = requests.get(f"https://api.countrystatecity.in/v1/countries/").json()
            return render_template('output.html', data=data, countrydata=countrydata)
           
        return render_template('error.html', data=data)
    
    return app





















#Material Icon Theme by Philipp Kief
#Pylance
#isort
#Python Extension Pack
#Python Indent
#autoDocstring - Python Docstring Generator by Nils Werner
#pip install python-restcountries
#https://github.com/SteinRobert/python-restcountries