import pytest
import requests
from weather_app import get_weather_data

@pytest.fixture
def api_key():
    return "70bc70821260784d5356823f60e659a9"

@pytest.fixture
def cities():
    return ["Mahi1212", "London"]

def test_get_weather_data(api_key, cities):
    weather_data = get_weather_data(api_key, cities)
    assert isinstance(weather_data, dict)
    assert len(weather_data) == len(cities)
    for city, data in weather_data.items():
        assert "weather" in data
        assert "main" in data["weather"][0]

def test_api_request_fail(api_key):
    # Test with an invalid city
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=InvalidCity&appid=" + api_key)
    assert response.status_code != 200

