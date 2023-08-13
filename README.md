# Projeto FMF - Análise de Sentimentos


Membros: Fabiano Caetano (líder), Fernando Mota, João Pedro, Lisandra Menezes, Marcos Vinicius e Pedro Saraiva


# Projeto de análise de sentimentos aplicado em bares goianos



Certamente análise de sentimentos é algo popular e uma questão resolvida pela academia, tanto é que podemos usar bibliotecas pré-treinadas para fazer essa análise. Nesse trabalho usamos alguns frameworks que fazem essa analise de sentimentos, algumas originais e outras sugeridas pelo artigo referencia: https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a.


Nosso objetivo com a análise de sentimentos não é identificar o estado da arte em análise de sentimento, mas quais são as aplicações nos negócios que são realmente valiosas. Queremos identificar padrões, gerar insights e ajudar a absorver os feedbacks dos clientes. Portanto, nosso projeto tem sua originalidade baseada no serviço posterior à análise de sentimento, pois simplesmente a predição de sentimentos não gera nenhum benefício por si só. 





# Ask


Nossa principal investigação é se a analise de sentimento ajuda na absorção de feedbacks dos clientes para com o negócio. Podemos separar essas perguntas em alguns tópicos primarios de investigação. Sem sombra de dúvidas, as perguntas poderiam ser ainda mais complexas, aqui vale ressaltar que é apenas uma exploração inicial com base em hipoteses. 


1 - Conseguirmos identificar os pontos fracos e fortes dos negócios na visão do cliente?


    1.1 - A partir dos comentários e dos pontos fracos e fortes as franquias seguem algum padrão?

    
    1.2 - Qual a frequência dos sentimentos? Conseguimos visualizar isso de alguma forma?


Em nossas considerações, percebemos que um produto viavel dessas analises seria um dashboard com gráficos.



# Get

1 - Scraping google 

    >>> scraping via plataforma apify --- forma mais rapida de validar se os dados do google maps respondem ao ask 

   
    >>> pipeline do processo de web scraping dos dados > implantação google (bs4 & selenium...)


    >>> Seguindo o caminho Model/AnalisesSentimento/dados.csv, você encontrará os dados da Big Query em um arquivo. Para acessar os comentários é necesário extrair do JSON "Review" com o seguinte código: 

            import pandas as pd
          
            caminho_arquivo = 'Caminho para o arquivo'
            
            dados = pd.read_csv(caminho_arquivo)
            
            def extrair_texto(review):
                try:
                    review_dict = eval(review)  # Avaliando a string como dicionário
                    texto = review_dict.get('text', None)
                    estrelas = review_dict.get('stars', None)
                    
                    return pd.Series([texto])
                except Exception as e:
                    return pd.Series([None, None])
            
            dados_reviews = dados['reviews'].dropna().apply(extrair_texto)
            dados_reviews.columns = ['texto']
            
            dados_reviews = dados_reviews[dados_reviews['texto'].notna()]
            
            
            dados_reviews.head()


# Explore -
    
     1 - Conseguirmos identificar os pontos fracos e fortes dos negócios na visão do cliente?

     
     >>> model/AnalisesSentimento/analiseComercial - Com nosso primeiro dataset, sem uso de IA, fizemos alguns agrupamentos para visualizar os melhores bares a partir da nota média dos comentários.
     
     >>>
     >>>
     >>>

     
     1.1 - A partir dos comentários e dos pontos fracos e fortes as franquias seguem algum padrão?
     >>>
     >>>

     
     1.2 - Qual a frequência dos sentimentos? Conseguimos visualizar isso de alguma forma?
     >>>
     >>>
     
# Model -


    textblob - Framework simples que trás várias funcionalidades para processamento de dados textuais. https://textblob.readthedocs.io/en/dev/


    SVC  model - O SVM é um tecnica que analisa e reconhece padrões, usando a classificação e análise de regressão. Como nossos dados são textuais, foi necessário a transformação em vetores. Outro ponto importante é que no treinamento do modelo, precisavamos de dados com anotação. Usamos as avaliações de 1 a 5 dos comentários no google maps para fazer a anotação dos dados.

    
    O modelo treinado se encontra no caminho model/SVC-model/modelo_treinado.pkl


    * Um grande desafio foi o idioma do dataset, como estamos fazendo uma prova de conceito, não focamos nos melhores modelos para dados em português, portanto, usamos a biblioteca TextBlob para traduzir todos os comentários. Tal arquivo se encontra no caminho model/SVC-model/comentarios-traduzidos.csv
    

# Comunication -

    >>> bd-extension.json => "Amplitude do nicho de mercado do segmento alimenticio."
    >>> bd-revies.json => "Dados segmento bar contendo as rewies de usuarios."
    >>> bd-reviews => "Desempacotador das reviws." --remonedado
    >>> df-coleta_manual => "Dados anotados manualmente."
    >>> df-no_review => "informações mais gerais sobre as lojas do segmento bar" --recomendado caso não precise usar as reviews."


