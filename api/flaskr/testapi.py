import requests
api = []
url = "https://api.countrystatecity.in/v1/countries/"

headers = {
  'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
}

response = requests.request("GET", url, headers=headers)
api.append(response.text)

print(api)
def requeststage1():
    api = []
    url = "https://api.countrystatecity.in/v1/countries/"
    headers = {
        'X-CSCAPI-KEY': 'MVB6MjhnMDB6OUtPTU9DR0pGUUxsYUl4YXFaNXhnSXVDbGk5VGVYcA=='
    }
    response = requests.request("GET", url, headers=headers)
    api.append(response.text)
