import json
import os
from flask import Flask, render_template, request
from .data import *
import requests
headers = {
    'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
}


response = requests.get(f'https://api.countrystatecity.in/v1/countries/', headers=headers)
responses = response.text
returned = json.loads(responses)



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
    

    
    @app.route('/Search_Country', methods=('GET', 'POST'))
    def GetPost():
        if request.method == 'POST':
            search = request.form['search']
            part1 = requests.get(f"https://api.countrystatecity.in/v1/countries/{search}", headers=headers)
            part2 = part1.text
            searchcountry = json.loads(part2)
            name = searchcountry['name']
            capital_country = searchcountry['capital']
            phonecode = searchcountry['phonecode']
            currency = searchcountry['currency']
            name_currency = searchcountry['currency_name']
            symbol_currency = searchcountry['currency_symbol']
            latitude = searchcountry['latitude']
            longitude = searchcountry['longitude']
            timezones = searchcountry['timezones']
            return render_template('search.html', data=data, capital_country=capital_country, name=name, phonecode=phonecode, currency=currency, name_currency=name_currency, symbol_currency=symbol_currency, timezones=timezones, latitude=latitude, longitude=longitude)

    
    @app.route('/Country_List')
    def listcountry():
        for x in returned:
            x = x['name']
            print(x)
            return render_template('countrylist.html', returned=returned)
    
    
    
    @app.route('/Country_List/<List>')
    def list_country(List):
        for x in returned:
            if List == x['name']:
                iso2 = x['iso2']    
                requestresponse = requests.get(f"https://api.countrystatecity.in/v1/countries/{iso2}", headers=headers)
                data1 = requestresponse.text
                parsejson = json.loads(data1)
                name = parsejson['name']
                capital_country = parsejson['capital']
                phonecode = parsejson['phonecode']
                currency = parsejson['currency']
                name_currency = parsejson['currency_name']
                symbol_currency = parsejson['currency_symbol']
                latitude = parsejson['latitude']
                longitude = parsejson['longitude']
                timezones = parsejson['timezones']
                # for x in timezones:
                    
                return render_template('output2.html', data=data, capital_country=capital_country, name=name, phonecode=phonecode, currency=currency, name_currency=name_currency, symbol_currency=symbol_currency, timezones=timezones, latitude=latitude, longitude=longitude)
            
        
    @app.route('/WorldMap/<country>')
    def output(country):
        for x in returned:
            if country == x['name']:
                iso2 = x['iso2']    
                requestresponse = requests.get(f"https://api.countrystatecity.in/v1/countries/{iso2}", headers=headers)
                data1 = requestresponse.text
                parsejson = json.loads(data1)
                name = parsejson['name']
                capital_country = parsejson['capital']
                phonecode = parsejson['phonecode']
                currency = parsejson['currency']
                name_currency = parsejson['currency_name']
                symbol_currency = parsejson['currency_symbol']
                timezones = parsejson['timezones']
                latitude = parsejson['latitude']
                longitude = parsejson['longitude']
                return render_template('output1.html', data=data, capital_country=capital_country, name=name, phonecode=phonecode, currency=currency, name_currency=name_currency, symbol_currency=symbol_currency, timezones=timezones, latitude=latitude, longitude=longitude)
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