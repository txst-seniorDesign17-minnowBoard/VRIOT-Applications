from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

def get_data():
    pass

@app.route('/')
def homepage():
    return "Senior Design Demo"

@ask.launch
def start_skill():
    welcome_message = "Hello, Welcome to the MinnowBoard Senior Design Project...Would you like to know who Randy's Best Friend is?"
    return question(welcome_message)

@ask.intent("YesIntent")
def say_bestie();
    bestie = "The way the legend of the Source God goes is ... There once was a man "

@ask.intent("NoIntent")
def no_bestie():
    randy = "Your name is probably Randy and this does not change things"
    return (randy)

if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0', port='80')