import requests

api_key = '9db4304536d30fbdf3bf4559885cf888'
city = input('please provide the city name:')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Tempratuur: {temp} K')
    print(f'Omschrijfing: {desc}')
else: 
    print('Fout bij het ophalen vand e gegevens sorry. Probeer het opnieuw.')
    