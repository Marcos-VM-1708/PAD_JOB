import pandas as pd
from transformers import pipeline
from refined_sentiment_analysis.bigquery_data_review import df

# predict 50mil lines
#-----------------------------------------------------------------
# run model:
classifier = pipeline("text-classification", model = 'bhadresh-savani/albert-base-v2-emotion')

# Split the data into batches of size 500
batch_size = 500
num_batches = len(df) // batch_size + (len(df) % batch_size != 0)
batches = [df[i * batch_size: (i + 1) * batch_size] for i in range(num_batches)]

results = []

#-----------------------------------------------------------------
# data predict:
for batch in batches:
    batch_data = batch["text"].tolist()
    truncated_data = [text[:512] for text in batch_data]

    # Perform sentiment analysis on the truncated data
    prediction = classifier(truncated_data)

    temp = pd.DataFrame(prediction)
    batch_results = pd.concat([temp, batch["text"]], axis = 1)
    results.append(batch_results)

final_result = pd.concat(results, ignore_index = True)

final_result.to_csv("predicao_albert.csv", index = False)

print(final_result.head())
print(final_result.shape)
