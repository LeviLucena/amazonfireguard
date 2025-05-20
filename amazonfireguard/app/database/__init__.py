from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Configura o banco no app Flask existente
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/frani/Documents/amazonfireguard/app/database/fireguard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
