from dotenv import load_dotenv
load_dotenv()

import os
import requests
## hide key 
api_key = os.environ['API_KEY']

city = input('please provide the city name:')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    celsius = temp - 273.15
    print(f'Tempratuur: {celsius:.2f}°C')
    desc = data['weather'][0]['description']
    print(f'Omschrijfing: {desc}')
else:
    print('Fout bij het ophalen vand de gegevens. probeer het opnieuw.')

 ## python3 weer_app.py