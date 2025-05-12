from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        senha = request.form['senha']
        # Aqui você pode adicionar lógica de autenticação
        print(f"Login com email: {email} e senha: {senha}")
        return redirect(url_for('home'))  # Redireciona para a home após login
    return render_template('login.html')

# Rota para a página de cadastro
