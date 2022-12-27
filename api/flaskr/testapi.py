from restcountries import RestCountryApiV2 as rapi

def foo(name):
    country_list = rapi.get_countries_by_name('France')