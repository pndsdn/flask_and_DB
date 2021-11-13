import requests
from flask import Flask, render_template, request, jsonify, redirect
import psycopg2
import json

app = Flask(__name__)


conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="pass123",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')

            if username == 'admin' and password == 'admin-pass':
                return redirect("/admin/")

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (username, password))
            if cursor.fetchone() is None:  # user not found
                return render_template('login.html', wrong='Wrong login or password')

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (username, password))
            records = list(cursor.fetchone())
            return render_template("account.html", user=records)

        elif request.form.get("registration"):
            return redirect("/registration/")

        elif request.form.get("delete"):
            log_del = request.form.get('log-for-del')
            cursor.execute("DELETE FROM service.users WHERE login=%s", (log_del,))
            conn.commit()

    return render_template('login.html')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_login = request.form.get('login')
        password = request.form.get('password')

        cursor.execute("SELECT login FROM service.users WHERE login=%s;", (new_login,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);", (str(new_name), str(new_login), str(password)))
            conn.commit()
            return redirect('/login/')

    return render_template('registration.html')


@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    cursor.execute("SELECT * FROM service.users")
    data_users = cursor.fetchall()
    return render_template('admin.html', db=data_users)


if __name__ == '__main__':
    app.run()
