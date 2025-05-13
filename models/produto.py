from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def atualizar_preco(self, novo_preco: float):
        if novo_preco < 0:
            raise ValueError("O novo preço não pode ser negativo.")
        self.preco = novo_preco

    def reduzir_estoque(self, quantidade: int):
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente.")
        self.estoque -= quantidade