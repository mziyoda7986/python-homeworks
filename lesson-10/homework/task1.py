import requests

def get_weather(name, key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': name,
        'appid': key,
        'units' : 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {name}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Description: {data['weather'][0]['description']}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Failed to retrieve weather data:", response.status_code, response.text)

key = 'e120d2088217e6ebdc23402be34aa2e1'
city = 'Tashkent'

get_weather(city, key)