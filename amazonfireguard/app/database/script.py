import os
from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///app/database/fireguard.db"

os.makedirs("app/database", exist_ok=True)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)"))
    print("Banco criado e conectado com sucesso.")
