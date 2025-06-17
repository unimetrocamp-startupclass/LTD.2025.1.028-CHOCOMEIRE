import os
from app import db, app

# Garante que a pasta "instance/" existe antes de criar o banco
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

# Cria as tabelas dentro do contexto da aplicação
with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")
