# Projeto FMF - Análise de Sentimentos


Membros: Fabiano Caetano (líder), Fernando Mota, João Pedro, Lisandra Menezes, Marcos Vinicius e Pedro Saraiva


# Projeto de análise de sentimentos aplicado em bares goianos



A Análise de Sentimentos é uma técnica utilizada para determinar a polaridade de uma sentença ou palavra, denominando o tom emocional da mensagem de positivo, negativo ou neutro. Nesse trabalho utilizamos alguns frameworks já estabelecidos e validados pela comunidade, com o intuito de identificar padrões, gerar insights e ajudar na absorção e processamento dos feedbacks dos clientes de maneira mais intuitiva.                                                                                                                        


# Ask


Utilizamos o artigo sugerido: [FMF](https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a) e adicionamos como característica original um novo conjunto de dados para o nosso trabalho, de modo que utilizando o conhecimento já existente (técnicas e frameworks do artigo citado) tentaremos responder as seguintes perguntas:

No [Ask](https://github.com/Marcos-VM-1708/PAD_JOB/tree/bf9ba97f1d542e9093c5b86ac770e5af9f3f8b1f/Ask) encontra-se os dados iniciais e modelos iniciais.

1 - Conseguirmos identificar os pontos fracos e fortes dos negócios na visão do cliente?


    1.1 - A partir dos comentários e dos pontos fracos e fortes as franquias seguem algum padrão?

    
    1.2 - Qual a frequência dos sentimentos? Conseguimos visualizar isso de alguma forma?


Sem sombra de dúvidas, as perguntas poderiam ser ainda mais complexas, aqui vale ressaltar que é apenas uma visualização com base em hipoteses. 

Em nossas considerações, percebemos que um produto viavel dessas analises seria um dashboard com gráficos.


# Get

Nessa etapa, do [Get](https://github.com/Marcos-VM-1708/PAD_JOB/tree/ac26b7437f58607af189d0f32520cd698a079030/Get) é a forma como extraímos nosso banco de dados e utilizamos dois principais métodos para a coleta de dados, sendo estes:

    1 - scraping via plataforma apify --- forma mais rapida de validar se os dados do google maps respondem ao ask 

   
    2 - pipeline do processo de web scraping dos dados > implantação google (bs4 & selenium...)


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
Armazenamos o conjunto de dados no [data_extracted](https://github.com/Marcos-VM-1708/PAD_JOB/tree/ac26b7437f58607af189d0f32520cd698a079030/data_extracted)

# Explore

Durante a fase de [explore](https://github.com/Marcos-VM-1708/PAD_JOB/tree/4ba73709c8fc8d84e0df24b4107db08ee5bbc777/explore) fizemos diversas modificações e alterações no dataset adquirido após a obtenção dos dados. Tratamos o nosso banco de dados para que o mesmo ficasse da melhor maneira possível para quando aplicarmos nossos modelos. Buscando responder as perguntas do Ask
    
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
     
# Model

Durante a modelagem utilizamos dois principais modelos, sendo eles:


    Textblob - Framework simples que trás várias funcionalidades para processamento de dados textuais. Um grande desafio foi o idioma do dataset, como estamos fazendo uma prova de conceito, não focamos nos melhores modelos para dados em português, portanto, usamos a biblioteca TextBlob para traduzir todos os comentários.
    Tal arquivo se encontra no caminho model/SVC-model/comentarios-traduzidos.csv
    https://textblob.readthedocs.io/en/dev/


    SVC  model - O SVM é um tecnica que analisa e reconhece padrões, usando a classificação e análise de regressão. Como nossos dados são textuais, foi necessário a transformação em vetores. Outro ponto importante é que no treinamento do modelo, precisavamos de dados com anotação. Usamos as avaliações de 1 a 5 dos comentários no google maps para fazer a anotação dos dados.
    O modelo treinado se encontra no caminho model/SVC-model/modelo_treinado.pkl

No fim, optamos por utilizar o SVC model, isso pois o nosso dataset e o dataset disponibilizado no projeto FMF eram extremamente similares, tornando o SVC model o modelo ideal para a predição de sentimentos.
    

# Comunication -

    >>> bd-extension.json => "Amplitude do nicho de mercado do segmento alimenticio."
    >>> bd-revies.json => "Dados segmento bar contendo as rewies de usuarios."
    >>> bd-reviews => "Desempacotador das reviws." --remonedado
    >>> df-coleta_manual => "Dados anotados manualmente."
    >>> df-no_review => "informações mais gerais sobre as lojas do segmento bar" --recomendado caso não precise usar as reviews."


