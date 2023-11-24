from flask import Flask, redirect, url_for, render_template 
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from zadanie import zadanie
from lab4 import lab4


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(zadanie)
app.register_blueprint(lab4)