import os
from flask import Flask, render_template, request
from .data import cards
import requests
# url = 'https://www.mapquestapi.com/staticmap/v5/map'
# response = requests.get(url)


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
        return render_template('base.html')
    
    @app.route('/WorldMap/<country>')
    def output(country):
        if country == country:
            return render_template('output.html')
        else:
            return render_template('error.html')
        
    @app.route('/<data>')
    def world(data):
        placeholder = []
        for x in cards['card']:
            placeholder.append(x['option'])
        if data == 'WorldMap':
            return render_template('world.html')
        elif data == 'SearchCountry':
            return render_template('search.html')
        elif data == 'CountryList':
            return render_template('countrylist.html')
        else:
            return render_template('error.html')

    return app





















#Material Icon Theme by Philipp Kief
#Pylance
#isort
#Python Extension Pack
#Python Indent
#autoDocstring - Python Docstring Generator by Nils Werner
#pip install python-restcountries
#https://github.com/SteinRobert/python-restcountries