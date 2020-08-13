import json
import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
parameters = {'APPID':'45d00ac6ea719f6cd2c444421bbb9328','q':'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
content = response.content
info = json.loads(content)
print(info)