import torch
from transformers import pipeline
import pandas as pd
from bigquery_data import df
#----------------------------------------------------------------
# imput data in pipeline:
data = df["text"][:740]
#----------------------------------------------------------------

classifier = pipeline("text-classification",model='bhadresh-savani/albert-base-v2-emotion')
prediction = classifier(data.tolist(), )
#----------------------------------------------------------------
def join_results(predict):
    temp = pd.DataFrame(predict)
    return pd.concat([temp, data], axis = 1)

dfn = join_results(prediction)
print(dfn.head())

"""
Description:
This script utilizes a powerful natural language processing model based on transfer learning,
specifically the 'bhadresh-savani/albert-base-v2-emotion' model, to classify sentiments
from Google Maps reviews. By analyzing the language used in these reviews, the model can
automatically determine the emotional tone conveyed in each review, helping businesses
and individuals gain valuable insights from user feedback."""