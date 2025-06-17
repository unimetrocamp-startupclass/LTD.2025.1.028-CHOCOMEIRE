from models import db  # Importando a instância global de db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def atualizar_preco(self, novo_preco: float) -> bool:
        """Atualiza o preço do produto, garantindo que seja válido."""
        if novo_preco < 0:
            return False  # Retorna False para evitar ValueError
        self.preco = novo_preco
        db.session.commit()
        return True  # Indica que a atualização foi bem-sucedida

    def reduzir_estoque(self, quantidade: int) -> bool:
        """Reduz o estoque do produto, evitando valores negativos."""
        if quantidade > self.estoque:
            return False  # Retorna False em vez de levantar um erro
        self.estoque -= quantidade
        db.session.commit()
        return True  # Indica que a operação foi concluída com sucesso

    def __repr__(self):
        """Representação do objeto Produto para facilitar debugging."""
        return f'<Produto {self.nome} - Preço: R${self.preco:.2f} - Estoque: {self.estoque}>'