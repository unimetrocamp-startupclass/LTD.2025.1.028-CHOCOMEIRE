from models import db  # Importa a instância global de db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def atualizar_email(self, novo_email: str):
        """Atualiza o email do cliente, garantindo que não esteja duplicado."""
        if Cliente.query.filter_by(email=novo_email).first():
            raise ValueError("Este e-mail já está em uso.")
        self.email = novo_email
        db.session.commit()

    @property
    def detalhes(self):
        """Retorna detalhes formatados do cliente."""
        return f"Nome: {self.nome}, Email: {self.email}"