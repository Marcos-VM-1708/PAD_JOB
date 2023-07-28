import requests
from bs4 import *
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.google.com/maps/search/restaurants/"
response = requests.get(url)
#-----------------------
# Get the Google Maps search results page for "restaurantes em São Paulo"
response = requests.get("https://www.google.com/maps/search/restaurantes+em+São+Paulo")
print(response)

def run_surch():
    chrome_driver_path = "chromedriver.exe"

    # Inicialize o navegador Chrome
    driver = webdriver.Chrome(executable_path = chrome_driver_path)
    driver.get(url)
# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
print(soup)

# Find all the restaurant results
restaurants = soup.find_all("div", class_="from_the_business")
print(restaurants)

def get_comment(url):
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = "html" # estrutura dos comentarios
    for comentario in resultados:
        # extrair os comentarios
        pass

if __name__ == '__main__':
    run_surch()
# Print the name, address, and rating of each restaurant
for restaurant in restaurants:
    name = restaurant.find("div", class_="business-name").text
    address = restaurant.find("div", class_="business-address").text
    rating = restaurant.find("div", class_="rating").text
    print(f"Name: {name}\nAddress: {address}\nRating: {rating}")