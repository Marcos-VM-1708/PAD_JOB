import os
import openai
import pandas as pd
from refined_sentiment_analysis.bigquery_data_review import filtered_rows
# --------------------------------------------------
openai.api_key = "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"
# --------------------------------------------------
data = filtered_rows["text"][:1]
data = data.reset_index(drop = True)
data = pd.DataFrame(data, columns=['text'])

# Definir parâmetros
batch_size = 1000  # Tamanho do lote
total_rows = len(data)
start_index = 0

# Mensagem do sistema
system_message = {
    "role": "system",
    "content": "voce é um classificador de sentimentos, identifique a emoção do texto em uma das opções. [critica, aprovação, duvida, fanatismo ]"
}

# Inicializar lista para armazenar saídas
outputs = []

# Processar em lotes
while start_index < total_rows:
    end_index = min(start_index + batch_size, total_rows)
    batch_data = data[start_index:end_index]

    messages = [system_message]

    for _, row in batch_data.iterrows():
        user_message = {"role": "user", "content": row["text"]}
        messages.append(user_message)
        assistant_message = {"role": "assistant"}
        messages.append(assistant_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.11,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.55,
        presence_penalty=0
    )

    # Processar a resposta da API
    assistant_reply = response.choices[0].message["content"]

    # Adicionar a saída ao DataFrame
    outputs.extend([{"predicao": assistant_reply, "texto": row["text"]} for _, row in batch_data.iterrows()])

    start_index = end_index

# Criar um DataFrame com as saídas
output_df = pd.DataFrame(outputs)

# Exibir ou salvar o DataFrame
print(output_df)
output_df.to_csv("gpt_predicao.csv", index=False)
