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






# import requests
# import json

# def get_weather(city_name):
#     api_key = "d2fba77adcd595f701d69814b3407245"  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

#     try:
#         response = requests.get(url)
#         data = json.loads(response.text)
        
#         if response.status_code == 200:
#             weather_info = data.get("weather")
#             main_info = data.get("main")
#             wind_info = data.get("wind")

#             if weather_info and main_info and wind_info:
#                 weather_description = weather_info[0].get("description")
#                 temperature = main_info.get("temp")
#                 humidity = main_info.get("humidity")
#                 wind_speed = wind_info.get("speed")

#                 print(f"Weather Forecast for {city_name}:")
#                 print(f"Description: {weather_description}")
#                 print(f"Temperature: {temperature} K")
#                 print(f"Humidity: {humidity}%")
#                 print(f"Wind Speed: {wind_speed} m/s")
#             else:
#                 print("Weather data not found.")
#         else:
#             error_message = data.get("message")
#             if error_message:
#                 print(f"Error: {error_message}")
#             else:
#                 print("Failed to retrieve weather data.")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     city = input("Enter the city name: ")
#     get_weather(city)
