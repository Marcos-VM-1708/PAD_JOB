import pandas as pd
from ask_2 import df
import matplotlib.pyplot as plt
from wordcloud import WordCloud

print(df.shape)
# print(df.columns)
#
# print(df["categoryName"].value_counts())


#------------------------------------------------------------------

def cloud_words(label):
    # Combine os dados da coluna desejada em um único texto
    text = ' '.join(label)

    # Crie a nuvem de palavras
    wordcloud = WordCloud(width = 800, height = 800,
                          background_color = 'white',
                          min_font_size = 10).generate(text)

    # Plote a nuvem de palavras usando o Matplotlib
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    # Exiba a nuvem de palavras
    plt.show()

