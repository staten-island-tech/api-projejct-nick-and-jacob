import os
from flask import Flask, render_template, request
import requests

url = 'https://www.mapquestapi.com/staticmap/v5/map'
response = requests.get(url)


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
    
    @app.route('/World/<data>')
    def world(data):
        if data == 'World':
            return request('base.html')
        else:
            return render_template('base.html')
    return app


























#Material Icon Theme by Philipp Kief
#Pylance
#isort
#Python Extension Pack
#Python Indent
#autoDocstring - Python Docstring Generator by Nils Werner
