from models import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    status = db.Column(db.String(50), default="Pendente")
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True, cascade="all, delete-orphan")

    def atualizar_status(self, novo_status: str) -> bool:
        status_validos = {"Pendente", "Em andamento", "Concluído", "Cancelado"}
        if novo_status not in status_validos:
            return False
        self.status = novo_status
        db.session.commit()
        return True

    def calcular_valor_total(self) -> float:
        return sum(item.produto.preco * item.quantidade for item in self.itens) if self.itens else 0.0

    def __repr__(self):
        return f'<Pedido {self.id} - Cliente {self.cliente_id} - Status: {self.status}>'

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    sabores = db.Column(db.String, nullable=True)

    produto = db.relationship('Produto', backref='itens_pedidos')

    def __repr__(self):
        return f'<ItemPedido {self.id} - Produto {self.produto_id} - Pedido {self.pedido_id} - Qtd: {self.quantidade}>'