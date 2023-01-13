# from restcountries import RestCountryApiV2 as rapi

# def foo(name):
#     country_list = rapi.get_countries_by_name('South Africa' ,filters=["name","currencies","capital"])
import requests


url = "https://api.countrystatecity.in/v1/countries"

headers = {
  'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
}

response = requests.request("GET", url, headers=headers)

print(response.text)