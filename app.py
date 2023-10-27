from flask import Flask, redirect, url_for, render_template 
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code = 302)

@app.route("/lab1")
def lab1():
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

@app.route("/menu")
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

        <a href="/lab1" target="_blank">Первая лабораторная</a>
        <a href="/lab2/" target="_blank">Вторая лабораторная</a>

        <footer>
            &copy; Елена Тарасова, ФБИ-12, 3 курс, 2023 
        </footer>
    <body>
</html>
"""
@app.route ("/lab1/oak")
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

@app.route("/lab1/student")
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

@app.route("/lab1/python")
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

@app.route("/lab1/Curtains")
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
@app.route('/lab2/example')
def example():
    name = 'Тарасова Елена'
    nomber = '2'
    group = ' ФБИ-12'
    course = ' 3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    book = [
        {'author': 'Джордж Оруэлл','name': '1984','genre': 'научная фантастика','pages': '328 стр.'},
        {'author': 'Лев Толстой','name': 'Война и мир','genre': 'роман','pages': '1392 стр.'},
        {'author': 'Джоан роулинг','name': 'Гарри Поттер и филосовский камень','genre': 'фэнтези','pages': '223 стр.'},
        {'author': 'Федор Достоевский','name': 'Преступление и наказание','genre': 'роман','pages': '671 стр.'},
        {'author': 'Эрих Мария Ремарк','name': 'Три товарища','genre': 'роман','pages': '448 стр.'},
        {'author': 'Михаил Булгаков','name': 'Мастер и Маргарита','genre': 'роман','pages': '480 стр.'},
        {'author': 'Олдос Хаксли','name': 'О дивный новый мир','genre': 'научная фантастика','pages': '288 стр.'},
        {'author': 'Пауло Коэльо','name': 'Алхимик','genre': 'роман','pages': '208 стр.'},
        {'author': 'Антуан де Сент-Экзюпери','name': 'Маленький принц','genre': 'сказка','pages': '96 стр.'},
        {'author': 'Лев Толстой','name': 'Анна Каренина','genre': 'роман','pages': '864 стр.'},
    ]
    return render_template('example.html', name=name,nomber=nomber, 
                            group=group, course=course, fruits=fruits,book=book)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/flowers/')
def flowers():
    return render_template('flowers.html')