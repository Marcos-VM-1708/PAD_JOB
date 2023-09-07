import os
import json
import pickle
import pandas as pd
from google.oauth2 import service_account

#------------------------------------------
# Carregue as informações do arquivo JSON
with open("GBQ.json", "r") as json_file:
    info = json.load(json_file)

# Crie as credenciais a partir das informações do arquivo JSON
credentials = service_account.Credentials.from_service_account_info(info)

# Pergunta
query = '''SELECT
            *
            FROM Refined_zone.explore_reviews'''

# Função para obter dados do BigQuery com cache
def get_bigquery_data(credentials, query):
    cache_filename = 'bigquery_cache.pkl'

    # Verifica se os dados estão em cache
    if os.path.exists(cache_filename):
        with open(cache_filename, 'rb') as cache_file:
            cached_data = pickle.load(cache_file)
            return cached_data

    # Caso os dados não estejam em cache, consulta o BigQuery
    df = pd.read_gbq(credentials=credentials, query=query)
    print(df.shape)
    # Armazena os dados em cache
    with open(cache_filename, 'wb') as cache_file:
        pickle.dump(df, cache_file)

    return df