import openai
import pandas as pd

# Configure sua chave de API
openai.api_key = "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"

# Função para classificar sentimentos
def classificar_sentimento(frase):
    prompt = f"Classifique o sentimento da seguinte frase, em uma das opções [aprovação, duvida, fanatismo, desaprovação] :\n'{frase}'\nSentimento:"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Escolha o mecanismo adequado
        prompt=prompt,
        temperature=0,              # Defina a temperatura de acordo com sua preferência
        max_tokens=500,              # Aumente este valor para permitir mais texto na resposta
        stop=None                   # Deixe a resposta aberta para qualquer sentimento
    )

    sentimento = response.choices[0].text.strip()
    return sentimento

# Exemplo de DataFrame
data = pd.read_csv("refined_data.csv")
data = data[:200]

# Aplicando a função à coluna 'texto'
data['sentimento'] = data['text_refined'].apply(classificar_sentimento)

data.to_csv("gpt_predição.csv",index=False)

print(data.head())
