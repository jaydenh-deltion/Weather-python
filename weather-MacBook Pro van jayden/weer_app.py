from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hallo, wereld!"
if __name__ == "__main__":
    app.run()


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
    daily_temp_max = data['main']['temp_max']
    celsius = temp - 273.15
    wind = data['wind']['speed']
    wind_deg = data['wind']['deg']
    rain = 'ja' if 'rain' in data['weather'][0]['main'] else 'nee'
    humidity = data['main']['humidity']
    alerts = data['alerts'] if 'alerts' in data else None
    desc = data['weather'][0]['description']

    



    print(f'Tempratuur: {celsius:.2f}°C')
    print(f'Maximale temperatuur: {daily_temp_max}°C')
    print(f'Omschrijfing: {desc}')
    print (f'Wind: {wind} m/s')
    print (f'Windrichting: {wind_deg}°')
    print(f'Neerslag: {rain}')
    print(f'luchtvochtigheid: {humidity}%')

    
else: 
    print('Error retrieving data, please try again.')

 ## python3 weer_app.py
 ## Park Village