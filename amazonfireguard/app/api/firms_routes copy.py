from flask import Blueprint, request, jsonify
import pandas as pd
import requests
from io import StringIO
import os

firms_bp = Blueprint('firms_bp', __name__)

def filtrar_amazonia(df):
    lat_min, lat_max = -20.0, 5.0
    lon_min, lon_max = -75.0, -50.0
    filtro = (
        (df['latitude'] >= lat_min) &
        (df['latitude'] <= lat_max) &
        (df['longitude'] >= lon_min) &
        (df['longitude'] <= lon_max)
    )
    return df.loc[filtro]

@firms_bp.route('/fires', methods=['GET'])
def fires():
    # usa parâmetro ?url= ou variável de ambiente FIRMS_API
    firms_api_url = request.args.get('url') or os.getenv('FIRMS_API')

    if not firms_api_url:
        return jsonify({"error": "URL da FIRMS não fornecida"}), 400

    print(f"🔍 URL usada: {firms_api_url}")  # VERIFICAR NO TERMINAL

    try:
        response = requests.get(firms_api_url)
        response.raise_for_status()

        df = pd.read_csv(StringIO(response.text))
        df_amz = filtrar_amazonia(df)

        cols = ['latitude', 'longitude', 'acq_date', 'bright_ti4', 'confidence']
        df_amz = df_amz[cols]

        return jsonify(df_amz.to_dict(orient='records'))
    except Exception as e:
        print(f"❌ Erro: {e}")
        return jsonify({"error": str(e)}), 500
