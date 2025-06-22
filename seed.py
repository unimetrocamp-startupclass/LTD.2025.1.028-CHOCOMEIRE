from app import app
from models import db
from models.produto import Produto

with app.app_context():
    if Produto.query.count() == 0:
        produtos = [
            Produto(
                nome="Cento de Docinhos",
                preco=110.0,
                estoque=10,
                imagem="docinhos1.png"
            ),
            Produto(
                nome="Meio Cento de Docinhos",
                preco=65.0,
                estoque=10,
                imagem="docinhos1.png"
            ),
            Produto(
                nome="Bombom Ao Leite (12un)",
                preco=30.0,
                estoque=20,
                imagem="imagem.bombom.jpg"
            ),
            Produto(
                nome="Bombons Sortidos (Branco, Meio Amargo, Licor, Crocante, Amendoim) - 12un",
                preco=36.0,
                estoque=20,
                imagem="imagem.bombom.jpg"
            )
        ]
        db.session.add_all(produtos)
        db.session.commit()
        print("✔️ Produtos adicionados com sucesso!")
    else:
        print("⚠️ Produtos já existem no banco. Nenhum item foi adicionado.")