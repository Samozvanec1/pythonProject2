from DZ import app
from flask import render_template, redirect, url_for, request

messages = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        if name and city and hobby and age:
            print(name, "\n", city, "\n", hobby, "\n", age)
            messages.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('index.html', messages=messages)