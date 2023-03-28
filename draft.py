#basic code to parse weather api, modify later to be more details and work with lambda & rds
import requests

def fetchWeather(city):
  URL = "http://api.openweathermap.org/data/2.5/weather?"
  PARAMS = {"appid": "c8efac34cc3548754ca009222d24da49", "q": city, "units": "imperial"}
  response = requests.get(url = URL, params = PARAMS).json()
  temperature = response["main"]["temp"]
  print(temperature)
  if temperature <= 65:
    print("You should wear a coat!")
  if temperature > 65:
    print("You are safe to wear shorts!")

userCity = input("Enter a city:")
fetchWeather(userCity)

