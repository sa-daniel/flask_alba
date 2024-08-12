from app import app
from flask import render_template

nome = 'Cabeça Dinossauro'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', página='Inícial', nome=nome)

@app.route('/contato')
def contato():
    return render_template('contato.html', página='Contato', nome=nome)
