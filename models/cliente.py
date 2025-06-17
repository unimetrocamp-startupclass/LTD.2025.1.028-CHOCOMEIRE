from models import db  # Importa a instância global de db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def atualizar_email(self, novo_email: str) -> bool:
        """Atualiza o email do cliente, garantindo que não esteja duplicado."""
        if Cliente.query.filter_by(email=novo_email).first():
            return False  # Retorna False se o email já estiver em uso
        self.email = novo_email
        db.session.commit()
        return True  # Retorna True se a atualização for bem-sucedida

    def __repr__(self):
        """Representação do objeto para facilitar a depuração."""
        return f'<Cliente {self.nome} ({self.email})>'