from flask import Flask, render_template, jsonify
import json
import requests

app = Flask(__name__)

METEO_API_KEY = ""
if METEO_API_KEY is None:
    METEO_API_KEY = "https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx"
else:
    METEO_API_KEY = "https://api.openweathermap.org/data/2.5/forecast?lat=48.883587&lon=2.333779&appid=" + METEO_API_KEY

@app.route('/api/meteo/')


def meteo():
    dictionnaire = {
        'type':"Prévision de température",
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrès Celcius"
    }
    return jsonify(dictionnaire)
@app.route("/")
def home():
    return ("<p>bonjours</p>")
app.run()

