from flask import Flask, render_template
from dotenv import load_dotenv
import os

from app.api import api_bp          # Importa seu blueprint de API
from app.database import init_db    # Inicializa o banco
from app.api.weather_routes import weather_bp
from app.api.firms_routes import firms_bp

load_dotenv()  # Carrega .env

def create_app():
    app = Flask(__name__)

    # Registra os blueprints
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(weather_bp, url_prefix="/api")
    app.register_blueprint(firms_bp, url_prefix="/api")

    # Inicializa banco
    init_db(app)

    # Rota principal renderiza index.html (com o mapa)
    @app.route('/')
    def home():
        return render_template('index.html')

    return app
