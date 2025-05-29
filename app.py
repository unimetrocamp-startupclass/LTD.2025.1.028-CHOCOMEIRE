from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para usar sessão!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

SABORES_LISTA = [
    'Brigadeiro', 'Brigadeiro Branco', 'Beijinho', 'Paçoquinha',
    'Moranguinho', 'Limão',
    'Casadinho (brigadeiro branco e tradicional)',
    'Sensação (brigadeiro tradicional e moranguinho)'
]

PRODUTOS = [
    {
        'id': 'cento',
        'nome': 'Docinhos Tradicionais (Cento - 100uni.)',
        'descricao': 'Cento (até 3 sabores)',
        'preco': 110.00,
        'imagem': 'docinhos1.png',
        'sabores': SABORES_LISTA,
        'limite_sabores': 3
    },
    {
        'id': 'meio_cento',
        'nome': 'Docinhos Tradicionais (Meio Cento - 50uni.)',
        'descricao': 'Meio Cento (até 2 sabores)',
        'preco': 65.00,
        'imagem': 'docinhos1.png',
        'sabores': SABORES_LISTA,
        'limite_sabores': 2
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    # Mostra o card agrupando os dois tamanhos
    return render_template('produtos.html', produtos=PRODUTOS[:1])

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    if product_id:
        cart = session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1
        session['cart'] = cart
        # Limpa sabores escolhidos para novo item
        sabores = session.get('sabores', {})
        if product_id not in sabores:
            sabores[product_id] = []
        session['sabores'] = sabores
    return jsonify({'success': True, 'cart': session.get('cart', {})})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    cart = session.get('cart', {})
    if product_id and product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] <= 0:
            del cart[product_id]
            # Remove sabores associados ao produto
            sabores = session.get('sabores', {})
            if product_id in sabores:
                del sabores[product_id]
            session['sabores'] = sabores
        session['cart'] = cart
    return jsonify({'success': True, 'cart': session.get('cart', {})})

@app.route('/carrinho')
def carrinho():
    cart = session.get('cart', {})
    sabores_selecionados = session.get('sabores', {})
    items = []
    total = 0.0
    for p in PRODUTOS:
        pid = p['id']
        if pid in cart:
            quantidade = cart[pid]
            subtotal = quantidade * p['preco']
            total += subtotal
            items.append({
                'id': pid,
                'nome': p['nome'],
                'imagem': p['imagem'],
                'quantidade': quantidade,
                'preco': p['preco'],
                'sabores': p['sabores'],
                'subtotal': subtotal,
                'limite_sabores': p['limite_sabores'],
                'sabores_escolhidos': sabores_selecionados.get(pid, [])
            })
    return render_template('carrinho.html', carrinho=items, total=total)

@app.route('/atualizar_sabores', methods=['POST'])
def atualizar_sabores():
    cart = session.get('cart', {})
    sabores = session.get('sabores', {})
    for p in PRODUTOS:
        pid = p['id']
        sabores_escolhidos = []
        for idx, sabor in enumerate(p['sabores']):
            key = f"sabores_{pid}_{idx}"
            if request.form.get(key):
                sabores_escolhidos.append(sabor)
        # Limita no servidor também (segurança extra)
        limite = p['limite_sabores']
        sabores[pid] = sabores_escolhidos[:limite]
    session['sabores'] = sabores
    return redirect(url_for('carrinho'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = User.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            print(f"Login bem-sucedido com email: {email}")
            return redirect(url_for('home'))
        else:
            print("Falha no login: email ou senha incorretos")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        print(f"Novo cadastro: {nome}, {email}")
        return redirect(url_for('home'))
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
