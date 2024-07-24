from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thesecretestkeyyouwillnothackbecauseitisverysecretpassword'
from flaskproject import routes