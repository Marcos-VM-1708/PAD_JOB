# Projeto FMF - Análise de Sentimentos


Membros: Fabiano Caetano (líder), Fernando Mota, João Pedro, Lisandra Menezes, Marcos Vinicius e Pedro Saraiva


# Projeto de análise de sentimentos aplicado em bares goianos



A Análise de Sentimentos é uma técnica utilizada para determinar a polaridade de uma sentença ou palavra, denominando o tom emocional da mensagem de positivo, negativo ou neutro. Nesse trabalho utilizamos alguns frameworks já estabelecidos e validados pela comunidade, com o intuito de identificar padrões, gerar insights e ajudar na absorção e processamento dos feedbacks dos clientes de maneira mais intuitiva.                                                                                                                        
    Cada pasta corresponde a um processo do modelo que foi seguido dentro do porjeto, por tanto, nos referênciamos no (AGEMC) Aks, Get, Explore, Model, Comunication.

# Ask


Utilizamos o artigo sugerido: (https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a) e adicionamos como característica original um novo conjunto de dados para o nosso trabalho, de modo que utilizando o conhecimento já existente (técnicas e frameworks do artigo citado) tentaremos responder as seguintes perguntas:


1 - Conseguirmos identificar os pontos fracos e fortes dos negócios na visão do cliente?


    1.1 - A partir dos comentários e dos pontos fracos e fortes as franquias seguem algum padrão?

    
    1.2 - Qual a frequência dos sentimentos? Conseguimos visualizar isso de alguma forma?


Sem sombra de dúvidas, as perguntas poderiam ser ainda mais complexas, aqui vale ressaltar que é apenas uma exploração inicial com base em hipoteses. 

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


