import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from models import db
from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido, ItemPedido

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'site.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo local
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

def get_usuario_logado():
    if 'usuario_id' in session:
        return User.query.get(session['usuario_id'])
    return None

def is_admin():
    usuario = get_usuario_logado()
    return usuario and usuario.email == "admin@chocomeire.com"

@app.route('/')
def home():
    usuario = get_usuario_logado()
    return render_template('index.html', usuario=usuario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = User.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('home'))
        else:
            flash("Email ou senha inválidos!", "error")
            return redirect(url_for('login'))

    usuario = get_usuario_logado()
    return render_template('login.html', usuario=usuario)

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

        if not nome or not email or not senha:
            flash("Todos os campos devem ser preenchidos!", "error")
            return redirect(url_for('cadastro'))

        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado!", "error")
            return redirect(url_for('cadastro'))

        senha_hash = generate_password_hash(senha)
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home'))

    usuario = get_usuario_logado()
    return render_template('cadastro.html', usuario=usuario)

@app.route('/produtos')
def produtos():
    usuario = get_usuario_logado()
    produtos = Produto.query.all()
    return render_template('produtos.html', usuario=usuario, produtos=produtos)

@app.route('/carrinho', methods=['GET', 'POST'])
def carrinho():
    usuario = get_usuario_logado()
    itens = []
    total = 0.0

    if request.method == 'POST':
        data = request.get_json()
        carrinho_data = data.get("carrinho", {})
        ids = [int(pid) for pid in carrinho_data.keys()]
        produtos = Produto.query.filter(Produto.id.in_(ids)).all()

        for produto in produtos:
            pid = str(produto.id)
            qtd = carrinho_data.get(pid, 0)
            subtotal = produto.preco * qtd
            itens.append({
                'id': produto.id,
                'nome': produto.nome,
                'imagem': produto.imagem,
                'preco': produto.preco,
                'quantidade': qtd,
                'subtotal': subtotal,
                'sabores': ["Brigadeiro", "Beijinho", "Moranguinho", "Limão", "Paçoquinha"],
                'limite_sabores': 3 if "cento" in produto.nome.lower() else 2,
                'sabores_escolhidos': []
            })
            total += subtotal

    return render_template("carrinho.html", usuario=usuario, carrinho=itens, total=total)

@app.route('/sincronizar-carrinho', methods=['POST'])
def sincronizar_carrinho():
    data = request.get_json()
    session['carrinho'] = data.get('carrinho', {})
    return jsonify({"status": "ok"})

@app.route('/finalizar-pedido', methods=['GET', 'POST'])
def finalizar_pedido():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        carrinho = session.get('carrinho', {})

        if not carrinho:
            flash("Seu carrinho está vazio!", "error")
            return redirect(url_for('produtos'))

        cliente = Cliente.query.filter_by(email=email).first()
        if not cliente:
            cliente = Cliente(nome=nome, email=email)
            db.session.add(cliente)
            db.session.commit()

        pedido = Pedido(cliente_id=cliente.id)
        db.session.add(pedido)
        db.session.commit()

        for produto_id_str, qtd in carrinho.items():
            produto_id = int(produto_id_str)
            item = ItemPedido(produto_id=produto_id, pedido_id=pedido.id, quantidade=qtd)
            db.session.add(item)

        db.session.commit()
        session['carrinho'] = {}

        flash("Pedido realizado com sucesso! 🎉", "success")
        return redirect(url_for('home'))

    usuario = get_usuario_logado()
    return render_template('checkout.html', usuario=usuario)

@app.route('/admin')
def admin_dashboard():
    if not is_admin():
        flash("Acesso restrito ao administrador!", "error")
        return redirect(url_for('home'))

    pedidos = Pedido.query.order_by(Pedido.id.desc()).all()
    return render_template("admin.html", usuario=get_usuario_logado(), pedidos=pedidos)

@app.route('/admin/pedido/<int:pedido_id>')
def admin_detalhes_pedido(pedido_id):
    if not is_admin():
        flash("Acesso restrito ao administrador!", "error")
        return redirect(url_for('home'))

    pedido = Pedido.query.get_or_404(pedido_id)
    cliente = pedido.cliente
    itens = ItemPedido.query.filter_by(pedido_id=pedido.id).all()
    produtos = []

    for item in itens:
        produto = Produto.query.get(item.produto_id)
        produtos.append({
            'nome': produto.nome,
            'quantidade': item.quantidade,
            'preco_unitario': produto.preco,
            'subtotal': item.quantidade * produto.preco
        })

    total = sum(p['subtotal'] for p in produtos)
    return render_template("admin_pedido.html", pedido=pedido, cliente=cliente, produtos=produtos, total=total)

if __name__ == '__main__':
    with app.app_context():
        os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
        db.create_all()
    app.run(debug=True)