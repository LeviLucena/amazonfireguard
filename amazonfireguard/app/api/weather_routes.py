from flask import Blueprint, request, jsonify
from app.services.weather import get_weather

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/weather', methods=['GET'])
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Parâmetros lat e lon são obrigatórios"}), 400

    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return jsonify({"error": "Parâmetros lat e lon devem ser números"}), 400

    data = get_weather(lat, lon)
    if data is None:
        return jsonify({"error": "Falha ao buscar dados meteorológicos"}), 500

    return jsonify(data)
