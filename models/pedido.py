from models import db  # Importando a instância global de db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    status = db.Column(db.String(50), default="Pendente")
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)

    def atualizar_status(self, novo_status: str):
        """Atualiza o status do pedido, garantindo que seja válido."""
        if novo_status not in {"Pendente", "Em andamento", "Concluído", "Cancelado"}:
            raise ValueError("Status inválido.")
        self.status = novo_status
        db.session.commit()

    def calcular_valor_total(self):
        """Calcula o valor total do pedido com base nos itens."""
        return sum(item.produto.preco * item.quantidade for item in self.itens) if self.itens else 0.0

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    produto = db.relationship('Produto', backref='itens_pedidos')  # Relacionamento com Produto