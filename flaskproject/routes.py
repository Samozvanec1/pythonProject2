# render_template отвечает за отображение html, redirect отвечает за перенаправление на другую страницу,
# url_for отвечает за построение ссылки, request отвечает за получение данных
from flaskproject import app
from flask import render_template, redirect, url_for, request

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        if name and email and message:
            messages.append({'name': name, 'email': email, 'message': message})
            return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('index.html', messages=messages)
