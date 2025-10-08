from datetime import datetime
from flask import Flask, render_template, request
from weather_v2 import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "London"

    weather_data = get_current_weather(city)

    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data['name'],
        status=weather_data['weather'][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        wind_speed=f"{weather_data['wind']['speed']:.1f}",
        today=datetime.fromtimestamp(weather_data['dt']).strftime("%d-%b-%Y"),
        sunrise=datetime.fromtimestamp(weather_data['sys']['sunrise']).time(),
        sunset=datetime.fromtimestamp(weather_data['sys']['sunset']).time()
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
