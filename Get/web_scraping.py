import requests
from bs4 import BeautifulSoup

# Get the Google Maps search results page for "restaurantes em São Paulo"
response = requests.get("https://www.google.com/maps/search/restaurantes+em+São+Paulo")


# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
print(soup)

# Find all the restaurant results
restaurants = soup.find_all("div", class_="from_the_business")
print(restaurants)

# Print the name, address, and rating of each restaurant
for restaurant in restaurants:
    name = restaurant.find("div", class_="business-name").text
    address = restaurant.find("div", class_="business-address").text
    rating = restaurant.find("div", class_="rating").text
    print(f"Name: {name}\nAddress: {address}\nRating: {rating}")