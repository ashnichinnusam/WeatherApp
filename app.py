from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '40450a3e911c19cc4fdd778b93fadc25'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    temp = None
    error = None
    city = ""

    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")

        if weather_data.json()['cod'] == '404':
            error = 'No city found. Please try again.'
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = weather_data.json()['main']['temp']

    return render_template('index.html', weather=weather, temp=temp, city=city, error=error)

if __name__ == '__main__':
    app.run(debug=True)


