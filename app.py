import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from argon2 import PasswordHasher

# Configuração da aplicação
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Definição do caminho absoluto para o banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'site.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados
db = SQLAlchemy(app)
ph = PasswordHasher()

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    messages = get_flashed_messages(with_categories=True)
    usuario = None
    if 'usuario_id' in session:
        usuario = User.query.get(session['usuario_id'])
    return render_template('index.html', messages=messages, usuario=usuario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = User.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id  # Armazena o ID na sessão
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('home'))
        else:
            flash("Email ou senha inválidos!", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for('home'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # Validação dos campos
        if not nome or not email or not senha:
            flash("Todos os campos devem ser preenchidos!", "error")
            return redirect(url_for('cadastro'))
        
        # Verificação de email duplicado
        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado!", "error")
            return redirect(url_for('cadastro'))

        # Hash seguro da senha
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home'))
    
    return render_template('cadastro.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

if __name__ == '__main__':
    with app.app_context():
        # Garantindo que a pasta instance exista antes de criar o banco
        os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
        db.create_all()
    app.run(debug=True)