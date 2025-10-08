from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="London"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "London"

    weather_data = get_current_weather(city)

    pprint(weather_data)

    # City is not found by API
    if not weather_data['cod'] == 200:
        print("\nCity not found!!!")
    else:
        todays_date = datetime.fromtimestamp(weather_data['dt'])
        sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
        print(f"\n Today's Date: {todays_date.date().strftime("%d-%b-%Y")}")
        print(f"\n Sunrise: {sunrise.time()}")
        print(f"\n Sunrise: {sunset.time()}")
