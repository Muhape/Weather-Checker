import requests

def get_weather(my_city):
    try:
        city = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={my_city}",timeout=10).json()
        if "results" not in city:
            return None
        city_info = city["results"]
        lat = city_info[0]["latitude"]
        lon = city_info[0]["longitude"]
        weather = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
        weather_temp = weather["current_weather"]["temperature"]
        return weather_temp
    except requests.exceptions.ReadTimeout:
        print(f"The weather service is taking too long. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong {e}")


while True:
    real_city = input("Type in a city(press enter to quit): ")
    if real_city == "":
        print("Thank you for using the program")
        break
    temp = get_weather(real_city)
    if temp is None:
        print(f"Sorry, I can't find your city {real_city} anywhere")
        continue
    else:
        print(f"Weather forecast for {real_city} is {temp}'c")
