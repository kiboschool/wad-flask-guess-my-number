from flask import Flask, render_template, request

import random

app = Flask(__name__)
SECRET_NUMBER = random.randint(1,99)

print("\n")
print("shhhh: the secret number is:", SECRET_NUMBER)
print("\n")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/game")
def game():
    return render_template("game.html")

@app.get("/guess/<n>")
def guess(n):
    return render_template("guess.html", guess=int(n), secret=SECRET_NUMBER)
