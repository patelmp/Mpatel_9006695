import requests

def get_weather_data(api_key, cities):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = {}

    for city in cities:
        params = {
            "q": city,
            "appid": api_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data[city] = response.json()
        else:
            print(f"Failed to get weather data for {city}: {response.status_code}")

    return weather_data

# Example usage
api_key = "70bc70821260784d5356823f60e659a9"
cities = ["London", "Paris", "New York", "Tokyo"]
weather_data = get_weather_data(api_key, cities)
for city, data in weather_data.items():
    print(f"Weather data for {city}: {data}")
