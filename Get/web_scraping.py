import requests
from bs4 import *
from selenium import webdriver

url = "https://www.google.com/maps/search/restaurants/"
response = requests.get(url)
#-----------------------

def run_surch():
    chrome_driver_path = "chromedriver.exe"

    # Inicialize o navegador Chrome
    driver = webdriver.Chrome(executable_path = chrome_driver_path)
    driver.get(url)


def get_comment(url):
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = "html" # estrutura dos comentarios
    for comentario in resultados:
        # extrair os comentarios
        pass

if __name__ == '__main__':
    run_surch()