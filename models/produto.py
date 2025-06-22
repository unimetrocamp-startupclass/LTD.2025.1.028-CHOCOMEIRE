from models import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    imagem = db.Column(db.String(200), nullable=True)

    def atualizar_preco(self, novo_preco: float) -> bool:
        if novo_preco < 0:
            return False
        self.preco = novo_preco
        db.session.commit()
        return True

    def reduzir_estoque(self, quantidade: int) -> bool:
        if quantidade > self.estoque:
            return False
        self.estoque -= quantidade
        db.session.commit()
        return True

    def __repr__(self):
        return f'<Produto {self.nome} - R${self.preco:.2f} - Estoque: {self.estoque}>'