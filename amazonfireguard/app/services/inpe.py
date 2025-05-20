import pandas as pd

def fetch_inpe_data():
    url = "http://queimadas.dgi.inpe.br/queimadas/portal-static/estatisticas_estados/"
    try:
        tables = pd.read_html(url)
        return tables[0]
    except Exception as e:
        print("Erro ao coletar dados do INPE:", e)
        return pd.DataFrame()
