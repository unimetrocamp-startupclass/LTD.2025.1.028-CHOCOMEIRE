from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de produtos
@app.route('/produtos')
def produtos():
    produtos = [
        {'nome': 'Produto 1', 'descricao': 'Delicioso chocolate'},
        {'nome': 'Produto 2', 'descricao': 'Chocolate ao leite'},
        {'nome': 'Produto 3', 'descricao': 'Chocolate branco'},
    ]
    return render_template('produtos.html', produtos=produtos)

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request
