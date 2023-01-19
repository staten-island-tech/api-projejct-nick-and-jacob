import json
import os
from flask import Flask, render_template
from .data import *
import requests
headers = {
    'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
}
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
        if Data == 'WorldMap':
            return render_template('world.html', data=data)
        elif Data == 'Search_Country':
            return render_template('search.html', data=data)
        else:
            return render_template('error.html', data=data)
    
    @app.route('/Country_List')
    def countrypage():
        response1 = requests.get(f'https://api.countrystatecity.in/v1/countries/', headers=headers)
        responses1 = response1.text
        returned1 = json.loads(responses1)
        name = returned1['name']
        return render_template('countrylist.html', data=data, name=name)
    
    @app.route('/Country_List/<data>')
    def countrylist(data):
        response = requests.get(f'https://api.countrystatecity.in/v1/countries/', headers=headers)
        responses = response.text
        returned = json.loads(responses)
        for x in returned:
            if data == x['name']:
                iso2 = x['iso2']    
                name = x['name']
                requestresponse = requests.get(f"https://api.countrystatecity.in/v1/countries/{iso2}", headers=headers)
                data1 = requestresponse.text
                parsejson = json.loads(data1)
                name_country = parsejson['name']
                capital_country = parsejson['capital']
                phonecode = parsejson['phonecode']
                currency = parsejson['currency']
                name_currency = parsejson['currency_name']
                symbol_currency = parsejson['currency_symbol']
                timezones = parsejson['timezones']
                latitude = parsejson['latitude']
                longitude = parsejson['longitude']
                return render_template('output.html', data=data, name=name, capital_country=capital_country, name_country=name_country, phonecode=phonecode, currency=currency, name_currency=name_currency, symbol_currency=symbol_currency, timezones=timezones, latitude=latitude, longitude=longitude)
        return render_template('error.html', data=data)
        
        
        
    @app.route('/WorldMap/<country>')
    def output(country):
        response = requests.get(f'https://api.countrystatecity.in/v1/countries/', headers=headers)
        responses = response.text
        returned = json.loads(responses)
        for x in returned:
            if country == x['name']:
                iso2 = x['iso2']    
                requestresponse = requests.get(f"https://api.countrystatecity.in/v1/countries/{iso2}", headers=headers)
                data1 = requestresponse.text
                parsejson = json.loads(data1)
                name_country = parsejson['name']
                capital_country = parsejson['capital']
                phonecode = parsejson['phonecode']
                currency = parsejson['currency']
                name_currency = parsejson['currency_name']
                symbol_currency = parsejson['currency_symbol']
                timezones = parsejson['timezones']
                latitude = parsejson['latitude']
                longitude = parsejson['longitude']
                return render_template('output.html', data=data, capital_country=capital_country, name_country=name_country, phonecode=phonecode, currency=currency, name_currency=name_currency, symbol_currency=symbol_currency, timezones=timezones, latitude=latitude, longitude=longitude)
        
        
        
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