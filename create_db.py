from app import app, db

# Executa dentro do contexto da aplicação
with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")
