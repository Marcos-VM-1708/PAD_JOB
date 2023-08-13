import torch
from refined_sentiment_analysis.bigquery_data import df
from transformers import AlbertTokenizer, AlbertForSequenceClassification
#----------------------------------------------------------------

# Carregar o tokenizer e o modelo
tokenizer = AlbertTokenizer.from_pretrained("bhadresh-savani/albert-base-v2-emotion")
model = AlbertForSequenceClassification.from_pretrained("bhadresh-savani/albert-base-v2-emotion")

#----------------------------------------------------------------

# Função para analisar emoções em um texto
def analyze_emotion(text):
    # Tokenizar o texto
    inputs = tokenizer(text, return_tensors = "pt", truncation = True, padding = True)

    # Passar os dados pelo modelo
    with torch.no_grad():
        outputs = model(**inputs)

    # Converter as saídas do modelo em probabilidades
    probabilities = torch.nn.functional.softmax(outputs.logits[0], dim = 0)

    # Decodificar as emoções
    emotion_labels = ["sadness", "fear", "anger", "joy", "neutral"]
    predicted_emotion = emotion_labels[probabilities.argmax().item()]

    return predicted_emotion, probabilities


# Função para exibir os resultados
def display_results(text, predicted_emotion, probabilities):
    print("Texto:", text)
    print("Emoção Predita:", predicted_emotion)
    print("Probabilidades:")
    for emotion, prob in zip(emotion_labels, probabilities):
        print(f"{emotion}: {prob:.4f}")


# Exemplo de uso
input_text = df["revies"].tolist()
predicted_emotion, probabilities = analyze_emotion(input_text)
display_results(input_text, predicted_emotion, probabilities)



