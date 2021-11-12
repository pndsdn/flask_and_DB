import requests
from flask import Flask, render_template, request
import psycopg2
import json

app = Flask(__name__)


conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="pass123",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'sadm1n' and password == 'pass-for-admin':
        return render_template('admin_page.html')

    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (username, password))
    records = list(cursor.fetchone())

    return render_template('account.html', full_name=records[1], title=records[2])


if __name__ == '__main__':
    app.run()