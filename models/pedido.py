from models import db  # Importando a instância global de db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    status = db.Column(db.String(50), default="Pendente")
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True, cascade="all, delete-orphan")

    def atualizar_status(self, novo_status: str) -> bool:
        """Atualiza o status do pedido, garantindo que seja válido."""
        status_validos = {"Pendente", "Em andamento", "Concluído", "Cancelado"}
        if novo_status not in status_validos:
            return False  # Evita a interrupção da aplicação por erro
        self.status = novo_status
        db.session.commit()
        return True  # Indica que a atualização foi bem-sucedida

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do pedido com base nos itens."""
        return sum(item.produto.preco * item.quantidade for item in self.itens) if self.itens else 0.0

    def __repr__(self):
        """Representação do objeto Pedido para facilitar debugging."""
        return f'<Pedido {self.id} - Cliente {self.cliente_id} - Status: {self.status}>'

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    produto = db.relationship('Produto', backref='itens_pedidos')

    def __repr__(self):
        """Representação do objeto ItemPedido."""
        return f'<ItemPedido {self.id} - Produto {self.produto_id} - Pedido {self.pedido_id} - Qtd: {self.quantidade}>'