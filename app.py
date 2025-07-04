import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask import send_file

from models import db
from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido, ItemPedido
from utils.pdf_utils import gerar_pdf_pedido

# IMPORTANTE: Adicione este import
from utils.carrinho_utils import montar_item_carrinho

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'site.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

def get_usuario_logado():
    if 'usuario_id' in session:
        return db.session.get(User, session['usuario_id'])
    return None

def is_admin():
    usuario = get_usuario_logado()
    return usuario and getattr(usuario, "is_admin", False)

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

@app.route('/meus-pedidos')
def meus_pedidos():
    usuario = get_usuario_logado()
    if not usuario:
        flash("É necessário estar logado para ver seus pedidos.", "error")
        return redirect(url_for('login'))

    cliente = Cliente.query.filter_by(email=usuario.email).first()
    if not cliente:
        flash("Cliente não encontrado.", "error")
        return redirect(url_for('home'))

    pedidos = Pedido.query.filter_by(cliente_id=cliente.id).order_by(Pedido.id.desc()).all()
    return render_template("meus_pedidos.html", usuario=usuario, pedidos=pedidos)

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

    if request.method == 'POST':
        try:
            data = request.get_json() or {}
            session['carrinho'] = data.get("carrinho", {})
            session['sabores_selecionados'] = json.dumps(data.get("sabores", {}))
            return jsonify({"status": "ok"})
        except Exception as e:
            return jsonify({"status": "erro", "mensagem": str(e)}), 500

    carrinho_data = session.get("carrinho", {})
    sabores_salvos = json.loads(session.get("sabores_selecionados", "{}"))
    ids = [int(pid) for pid in carrinho_data.keys()]
    produtos = Produto.query.filter(Produto.id.in_(ids)).all()

    itens = []
    total = 0.0

    # NOVA LÓGICA: usa a função utilitária para montar cada item conforme as regras de limite de sabores
    for produto in produtos:
        pid = str(produto.id)
        qtd = carrinho_data.get(pid, 0)
        sabores_escolhidos = sabores_salvos.get(pid, [])
        item = montar_item_carrinho(produto.__dict__, qtd, sabores_escolhidos)
        itens.append(item)
        total += item['subtotal']

    return render_template("carrinho.html", usuario=usuario, carrinho=itens, total=total)

@app.route('/finalizar-pedido', methods=['GET', 'POST'])
def finalizar_pedido():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        carrinho = session.get('carrinho', {})
        sabores_selecionados = json.loads(session.get('sabores_selecionados', '{}'))

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
            lista_sabores = sabores_selecionados.get(produto_id_str, [])
            sabores_str = ",".join(lista_sabores)
            item = ItemPedido(produto_id=produto_id, pedido_id=pedido.id, quantidade=qtd, sabores=sabores_str)
            db.session.add(item)

        db.session.commit()
        session.pop('carrinho', None)
        session.pop('sabores_selecionados', None)

        flash("Pedido realizado com sucesso! 🎉", "success")
        return redirect(url_for('home'))

    usuario = get_usuario_logado()
    carrinho = session.get('carrinho', {})
    sabores = json.loads(session.get("sabores_selecionados", "{}"))
    produtos = Produto.query.filter(Produto.id.in_([int(pid) for pid in carrinho.keys()])).all()
    produtos_map = {str(p.id): p for p in produtos}

    return render_template('checkout.html', usuario=usuario, carrinho=carrinho, sabores=sabores, produtos=produtos_map)

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
            'subtotal': item.quantidade * produto.preco,
            'sabores': item.sabores
        })

    total = sum(p['subtotal'] for p in produtos)
    return render_template("admin_pedido.html", pedido=pedido, cliente=cliente, produtos=produtos, total=total)

@app.route('/admin/pedido/<int:pedido_id>/atualizar-status', methods=['POST'])
def atualizar_status_pedido(pedido_id):
    if not is_admin():
        flash("Acesso restrito ao administrador!", "error")
        return redirect(url_for('home'))

    novo_status = request.form.get("status")
    pedido = Pedido.query.get_or_404(pedido_id)
    pedido.status = novo_status
    db.session.commit()

    flash("Status do pedido atualizado!", "success")
    return redirect(url_for('admin_detalhes_pedido', pedido_id=pedido.id))


@app.route('/admin/pedido/<int:pedido_id>/excluir', methods=['POST'])
def excluir_pedido(pedido_id):
    if not is_admin():
        flash("Acesso restrito ao administrador!", "error")
        return redirect(url_for('home'))

    pedido = Pedido.query.get_or_404(pedido_id)
    db.session.delete(pedido)
    db.session.commit()

    flash("Pedido excluído com sucesso!", "success")
    return redirect(url_for('admin_dashboard'))

@app.route('/meus-pedidos/<int:pedido_id>/pdf')
def baixar_pdf_pedido(pedido_id):
    usuario = get_usuario_logado()
    if not usuario:
        flash("É necessário estar logado para baixar o pedido.", "error")
        return redirect(url_for('login'))

    pedido = Pedido.query.get_or_404(pedido_id)

    # Garante que o pedido pertence ao usuário logado
    if pedido.cliente.email != usuario.email:
        flash("Você não tem permissão para acessar esse pedido.", "error")
        return redirect(url_for('meus_pedidos'))

    pdf_path = gerar_pdf_pedido(pedido)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
        db.create_all()
    app.run(debug=True)