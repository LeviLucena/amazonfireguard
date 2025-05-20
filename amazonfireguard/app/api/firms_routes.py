from flask import Blueprint, request, jsonify
import pandas as pd
import requests
from io import StringIO
import os

firms_bp = Blueprint('firms_bp', __name__)

@firms_bp.route('/fires', methods=['GET'])
def fires():
    firms_api_url = request.args.get('url') or os.getenv('FIRMS_API')

    if not firms_api_url:
        return jsonify({"error": "URL da FIRMS não fornecida"}), 400

    print(f"🔍 URL usada: {firms_api_url}")

    try:
        response = requests.get(firms_api_url)
        response.raise_for_status()

        df = pd.read_csv(StringIO(response.text))
        # Sem filtro
        df_amz = df  

        cols = ['latitude', 'longitude', 'acq_date', 'bright_ti4', 'confidence']
        df_amz = df_amz[cols]

        return jsonify(df_amz.to_dict(orient='records'))
    except Exception as e:
        print(f"❌ Erro: {e}")
        return jsonify({"error": str(e)}), 500

