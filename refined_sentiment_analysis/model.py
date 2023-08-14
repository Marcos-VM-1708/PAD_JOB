import torch
from transformers import pipeline
import pandas as pd
from bigquery_data_review import filtered_rows

# Define the maximum sequence length supported by the model
MAX_SEQ_LENGTH = 512

# Extract the first 740 reviews
data = filtered_rows["text"]


truncated_data = [text[:MAX_SEQ_LENGTH] for text in data]

# Create a text classification pipeline with the model
classifier = pipeline("text-classification", model='bhadresh-savani/albert-base-v2-emotion')

# Perform sentiment analysis on the truncated data
prediction = classifier(truncated_data)

# Define a function to join the results
def join_results(predict, original_data):
    temp = pd.DataFrame(predict)
    return pd.concat([temp, original_data], axis=1)

# Join the prediction results with the original review text
dfn = join_results(prediction, filtered_rows[["text","title", "stars"]])

# Print the first few rows of the resulting DataFrame
dfn.to_csv("predição.csv")
print(dfn.head())
