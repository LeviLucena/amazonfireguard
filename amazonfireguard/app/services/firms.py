import requests
import pandas as pd
from io import StringIO

def fetch_firms_csv(url: str, timeout: int = 15) -> pd.DataFrame | None:
    """
    Baixa dados de focos de queimadas (FIRMS) em formato CSV a partir da URL fornecida,
    e retorna um DataFrame pandas com colunas relevantes.

    Parâmetros:
    - url (str): URL completa da API FIRMS que retorna o CSV dos focos.
    - timeout (int): tempo máximo em segundos para aguardar a resposta HTTP (padrão: 15).

    Retorna:
    - pandas.DataFrame com colunas filtradas e renomeadas.
    - None caso haja erro na requisição ou no parsing do CSV.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        # Lê o CSV recebido em memória
        df = pd.read_csv(StringIO(response.text))

        # Verifica se colunas esperadas existem
        required_columns = {'latitude', 'longitude', 'acq_date', 'confidence', 'frp'}
        if not required_columns.issubset(df.columns):
            print(f"CSV recebido não contém todas as colunas esperadas: {required_columns}")
            return None

        # Filtra e renomeia as colunas para simplificar o uso no frontend
        df = df[['latitude', 'longitude', 'acq_date', 'confidence', 'frp']]
        df = df.rename(columns={
            'acq_date': 'data',
            'confidence': 'confianca',
            'frp': 'potencia'
        })

        return df

    except requests.RequestException as e:
        print(f"Erro na requisição à API FIRMS: {e}")
    except pd.errors.ParserError as e:
        print(f"Erro ao processar CSV recebido da API FIRMS: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None
