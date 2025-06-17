from models import db  # Importando a instância global de db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def atualizar_preco(self, novo_preco: float):
        """Atualiza o preço do produto, garantindo que seja válido."""
        if novo_preco < 0:
            raise ValueError("O novo preço não pode ser negativo.")
        self.preco = novo_preco
        db.session.commit()

    def reduzir_estoque(self, quantidade: int):
        """Reduz o estoque do produto, evitando valores negativos."""
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente.")
        self.estoque -= quantidade
        db.session.commit()