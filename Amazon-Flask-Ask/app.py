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