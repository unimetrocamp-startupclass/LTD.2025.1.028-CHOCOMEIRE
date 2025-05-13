from app import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    status = db.Column(db.String(50), default="Pendente")
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)

    def atualizar_status(self, novo_status: str):
        if novo_status not in {"Pendente", "Em andamento", "Concluído", "Cancelado"}:
            raise ValueError("Status inválido.")
        self.status = novo_status

    def calcular_valor_total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens)

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)