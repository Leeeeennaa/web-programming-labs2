from flask import Flask, redirect, url_for, render_template, session 
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from zadanie import zadanie
from lab4 import lab4
from lab5 import lab5
from lab8 import lab8
from lab9 import lab9
from lb7 import lb7


app = Flask(__name__)
app.secret_key = '12345'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(zadanie)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(lb7)