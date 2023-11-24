from flask import Blueprint, redirect, url_for 
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code = 302)


@lab1.route("/lab1")
def lab():
    return """
<!doctype html>
<html>
    <head>
        <title>Тарасова Елена Дмитриевна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <div>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</div><br>

        <h2>Рализованные роуты</h2>

        <a href="http://127.0.0.1:5000/lab1/python" target="_blank">ПИТОН</a>
        <a href="http://127.0.0.1:5000/lab1/student" target="_blank">ПРО СТУДЕНТА</a>
        <a href="http://127.0.0.1:5000/lab1/Curtains" target="_blank">ШТОРКИ</a>

        <footer>
            &copy; Елена Тарасова, ФБИ-12, 3 курс, 2023 
        </footer>
    <body>
</html>
"""


@lab1.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>Меню</h1>

        <a href="/lab1" target="_blank">Первая лабораторная</a><br>
        <a href="/lab2/" target="_blank">Вторая лабораторная</a><br>
        <a href="/lab3/" target="_blank">Третья лабораторная</a><br>
        <a href="/lab4/" target="_blank">Четвертая лабораторная</a><br>

        <footer>
            &copy; Елена Тарасова, ФБИ-12, 3 курс, 2023 
        </footer>
    <body>
</html>
"""


@lab1.route ("/lab1/oak")
def oak ():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css') +'''">
    </head>
        <body>
            <main>
                <h1>Дуб</h1>
                <img src="'''+ url_for('static', filename='oak.jpg') +'''"> 
            </main>   
        </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css') +'''">
    </head>
        <body>
            <main>
                <h1>Тарасова Елена Дмитриевна</h1>
                <img src="'''+ url_for('static', filename='NSTU.jpg') +'''"> 
            </main>   
        </body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css') +'''">
    </head>
        <body>
            <main>
                <h1>Python</h1>
                <div>Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения,
                 науке о данных и машинном обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении и работает 
                 на разных платформах. Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость
                 разработки.</div>
                <img src="'''+ url_for('static', filename='python.jpg') +'''"> 
            </main>   
        </body>
</html>
'''


@lab1.route("/lab1/Curtains")
def Curtains():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css') +'''">
    </head>
        <body>
            <main>
                <h1>Шторы</h1>
                <div>В русском языке самое раннее появление слова «штора» отмечено, первоначально в виде «стора», в 1707 году 
                (в форме мн. ч. «сторы»)[1], так оно было заимствовано из французского (фр. store), куда пришло из латинского (лат. storea),
                 означающего «рогожа», «циновка»</div>
                <img src="'''+ url_for('static', filename='Curtains.jpg') +'''"> 
            </main>   
        </body>
</html>
'''