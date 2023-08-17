import re
from refined_sentiment_analysis.bigquery_data_review import df
import nltk
import pandas as pd

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

#----------------------------------------------------
# especial caracteres:
def remove_special_characters(column):
    cleaned_column = column.apply(lambda x: re.sub(r'[^a-zA-Z]', '', x))
    print("process_1")
    return cleaned_column
df["text_refined"] = remove_special_characters(df["text"])
#----------------------------------------------------
# upercases:
def lowercase_column(column):
    if isinstance(column, pd.Series):
        print("process_2")
        return column.str.lower()
    else:
        raise ValueError("Input should be a pandas Series.")
df["text_refined"] = lowercase_column(df["text"])
#----------------------------------------------------

def remove_stopwords_from_column(dataframe):

    stop_words = set(stopwords.words("portuguese"))
    print("process_3")
    def remove_stopwords(text):
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    dataframe = dataframe.apply(remove_stopwords)

    return dataframe

df["text_refined"] = remove_stopwords_from_column(df["text_refined"])
#----------------------------------------------------
def preprocess_column(text_column):
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    stop_words = set(stopwords.words('portuguese'))

    preprocessed_texts = []

    for text in text_column:
        # Tokenização
        words = word_tokenize(text)

        # Remoção de stopwords
        words = [word for word in words if word.lower() not in stop_words]

        # Stemming
        stemmed_words = [stemmer.stem(word) for word in words]

        # Lematização usando WordNet POS tags
        lemmatized_words = []
        for word in words:
            pos_tag = nltk.pos_tag([word])[0][1][0].upper()
            pos_tag = pos_tag if pos_tag in ['N', 'V', 'R', 'J'] else wordnet.NOUN
            lemmatized_words.append(lemmatizer.lemmatize(word, pos = pos_tag))

        preprocessed_texts.append(' '.join(lemmatized_words))

    return preprocessed_texts

# df["text_refined"] = preprocess_column(df["text_refined"])
#----------------------------------------------------
def extra_spaces(column):
    cleaned_column = []
    print("process_4")
    for item in column:
        cleaned_item = ' '.join(item.split())  # Remove extra spaces
        cleaned_column.append(cleaned_item)
    return cleaned_column
df["text_refined"] = extra_spaces(df["text_refined"])
print(df["text_refined"])

#----------------------------------------------------

df.to_csv("refined_data.csv")
print(df.shape)