from flask import Flask, request
from os import getenv

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Server started in port {getenv("PORT")}'
