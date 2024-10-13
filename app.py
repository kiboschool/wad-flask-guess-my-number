from flask import Flask, render_template, request

import random

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")
