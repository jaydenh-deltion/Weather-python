import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ['API_KEY']
city = input('please provide the city name:')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    celsius = temp - 273.15
    desc = data['weather'][0]['description']
    print(f'Tempratuur: {celsius:.2f}°C')
    print(f'Omschrijfing: {desc}')
else: 
    print('Error retrieving data, please try again.')

 ## python3 weer_app.py