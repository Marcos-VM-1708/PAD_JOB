from google.cloud import bigquery

client = bigquery.Client()
projeto = 'seu-projeto'
conjunto_dados = 'seu-conjunto-de-dados'
nome_tabela = 'minha_tabela'


novas_colunas = bigquery.SchemaField("text_refined", "STRING")

# Obtém a referência da tabela
tabela_ref = f"{projeto}.{conjunto_dados}.{nome_tabela}"

# Obtém informações da tabela atual
tabela = client.get_table(tabela_ref)

# Adiciona as novas colunas à tabela
tabela.schema += novas_colunas

# Atualiza a tabela com o novo esquema
tabela = client.update_table(tabela, ["schema"])

print(f"Colunas adicionadas com sucesso à tabela {tabela_ref}")
