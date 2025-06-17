import os
from app import db, app

# Garante que a pasta "instance/" existe
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

with app.app_context():
    db.create_all()
