import requests
import os

def get_weather(lat, lon):
    api_key = os.getenv("METEOBLUE_API_KEY")
    if not api_key:
        raise ValueError("METEOBLUE_API_KEY não está configurada no ambiente")

    url = f"https://my.meteoblue.com/packages/basic-day?lat={lat}&lon={lon}&apikey={api_key}&format=json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lança exceção se status != 200
        return response.json()
    except requests.RequestException as e:
        # Logar o erro, ou tratar de forma apropriada
        print(f"Erro ao consultar API do Meteoblue: {e}")
        return None
