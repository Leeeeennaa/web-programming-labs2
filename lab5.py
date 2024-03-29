from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 =Blueprint("lab5", __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base_for_tarasova_elena",
        user="tarasova_elena_knowledge_base",
        password="12345")
    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route("/lab5/")

def main():
    visibleUser = "Anon"
    visibleUser=session.get('username')

    return render_template('lab5.html', username=visibleUser)

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def regPage():
    errors = ""

    if request.method == "GET":
        return render_template('register.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')
   
    if not (username or password):
        errors = "Пожалуйтса, заполните все поля"
        print(errors)
        return render_template("register.html", errors=errors)
    
    hashPassword = generate_password_hash(password)
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors = "Пользователь с данным именем уже существует"
        dbConnect(cur,conn)
        return render_template('register.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    dbClose(cur,conn)

    return redirect('/lab5/login')

@lab5.route('/lab5/login', methods = ['GET', 'POST'])
def logPage():
    errors = "";

    if request.method == "GET":
        return render_template('login.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')
    
    if not (username or password):
        errors = "Пожалуйтса, заполните все поля"
        return render_template("login.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor() 

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}';")

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template("login.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect('/lab5/')
    else:
        errors = "Неправильный логин или пароль"
        return render_template("login.html", errors=errors)

@lab5.route("/lab5/new_arсticle", methods=["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")

        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")

            new_arcticle_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_arcticle_id}")
    return redirect ("/lab5/login")

@lab5.route('/lab5/new_arсticle/<string:arcticle_id>')
def getArticle(arcticle_id):
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()     

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (arcticle_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            
            return "Not found"
        
        text = articleBody[1].splitlines()

        return render_template('articleN.html', article_text = text, 
article_title=articleBody[0], username = session.get('username'))

@lab5.route("/lab5/articles_all")
def seeArticle():
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        cur.execute(f"SELECT title FROM articles WHERE user_id = '{userID}'")

        articleBody = cur.fetchall()

        dbClose(cur,conn)

        if articleBody is None:
            return "Not found!"
        return render_template("articleAll.html", article_title=articleBody, username=session.get("username"))

@lab5.route("/lab5/logout")
def logOut():

    session.clear()
    return render_template('lab5.html')