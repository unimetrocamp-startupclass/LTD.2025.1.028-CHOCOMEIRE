from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def atualizar_email(self, novo_email: str):
        if Cliente.query.filter_by(email=novo_email).first():
            raise ValueError("Este e-mail já está em uso.")
        self.email = novo_email

    def mostrar_detalhes(self):
        return f"Nome: {self.nome}, Email: {self.email}"