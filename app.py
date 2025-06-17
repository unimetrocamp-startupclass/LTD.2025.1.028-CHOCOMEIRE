from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from argon2 import PasswordHasher

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = User.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, senha):
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('home'))
        else:
            flash("Email ou senha inválidos!", "error")
            return redirect(url_for('login'))
    
    return render_template('login.html')

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
        senha_hash = ph.hash(senha)
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home'))
    
    return render_template('cadastro.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)