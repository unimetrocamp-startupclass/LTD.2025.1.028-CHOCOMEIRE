from flask_sqlalchemy import SQLAlchemy

# Inicializando a instância global do banco de dados
db = SQLAlchemy()

# Importando os modelos para garantir que sejam registrados corretamente no SQLAlchemy
from models.cliente import Cliente
from models.pedido import Pedido
from models.produto import Produto

# Garantindo que o modelo `ItemPedido` seja importado apenas se existir
try:
    from models.item_pedido import ItemPedido
except ImportError:
    ItemPedido = None