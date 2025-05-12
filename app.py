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
        email = request.form['email']
        senha = request.form['senha']  # Corrigido para pegar a senha corretamente
        usuario = User.query.filter_by(email=email).first()
        
        # Verifica se o usuário existe e se a senha está correta
        if usuario and check_password_hash(usuario.senha, senha):
            print(f"Login bem-sucedido com email: {email}")
            return redirect(url_for('home'))  # Redireciona para a home após login
        else:
            print("Falha no login: email ou senha incorretos")
            return redirect(url_for('login'))  # Volta para a página de login
    return render_template('login.html')

# Rota para a página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        # Cria um hash da senha antes de salvar no banco de dados
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        print(f"Novo cadastro: {nome}, {email}")
        return redirect(url_for('home'))  # Redireciona para a home após o cadastro
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
