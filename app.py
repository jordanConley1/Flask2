from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/myname/<word>/<word1>/<word2>')
def myname(word,word1,word2):
    return '<h1>{}</h1>'.format(escape(word.capitalize())+' '+escape(word1.capitalize())+' '+escape(word2.capitalize()))
