from flask_sqlalchemy import SQLAlchemy

# Inicializando a instância global do banco de dados
db = SQLAlchemy()

# Importando os modelos para garantir que sejam reconhecidos pelo SQLAlchemy
from models.cliente import Cliente
from models.pedido import Pedido
from models.produto import Produto
from models.item_pedido import ItemPedido  # Se houver esse modelo