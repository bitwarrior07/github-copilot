import requests
import json

def get_weather(city):
    """Gets the current weather forecast for the given city."""
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}".format(city)
    api_key = "d2fba77adcd595f701d69814b3407245"

    response = requests.get(api_url, headers={"Authorization": "Bearer {}".format(api_key)}, verify=False)
    if response.status_code == 200:
        weather_data = json.loads(response.content)
        return weather_data
    else:
        raise Exception("Error getting weather data: {}".format(response.status_code))

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather(city)

    print("Current weather in {}:".format(city))
    print("Temperature: {} degrees Celsius".format(weather_data["main"]["temp"]))
    print("Humidity: {}%".format(weather_data["main"]["humidity"]))
    print("Wind speed: {} kilometers per hour".format(weather_data["wind"]["speed"]))

if __name__ == "__main__":
    main()
