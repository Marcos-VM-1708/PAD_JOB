import pandas as pd

from ask_2 import df
from transformers import pipeline
from transformers import AutoTokenizer

model_name = "bhadresh-savani/albert-base-v2-emotion"

unlabeled_data = df['text'].head(100).tolist()

tokenizer = AutoTokenizer.from_pretrained(model_name)



classifier = pipeline("text-classification", model = model_name, return_all_scores=True)
prediction = classifier(unlabeled_data)

print(prediction)

temp = pd.DataFrame(prediction)
dfn = 




