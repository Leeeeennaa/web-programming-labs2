from flask import Blueprint, redirect, url_for 
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/flowers/')
def flowers():
    return render_template('flowers.html')