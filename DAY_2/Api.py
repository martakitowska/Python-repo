import requests
import json

user_name = input('Podaj swoje imię: ')

get_parameters = {"name": user_name, "country_id": "PL"}
content = requests.get('https://api.genderize.io', params=get_parameters)
dict = json.loads(content.text)

print('Jesteś "' + dict['gender'] + '" z prawdopodobieństwem: ' + str(dict['probability'] * 100) + '%')