import os
import requests

API_KEY = os.getenv("OWM_KEY")

parameters = {
    "lat": -23.5506507,
    "lon": -46.6333824,
    "appid": API_KEY
}

api_url = f"https://api.openweathermap.org/data/2.5/weather"

response = requests.get(api_url, params=parameters)

data = response.json()

print(data)