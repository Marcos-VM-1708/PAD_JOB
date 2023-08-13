from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def scrape_google_maps_reviews(url):
    # Configurar o Chrome WebDriver usando a variável de ambiente PATH
    driver = webdriver.Chrome()

    # Navegar até a página do local no Google Maps
    driver.get(url)

    try:
        # Esperar até que as avaliações sejam carregadas (pode variar dependendo da conexão)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "section-review-content"))
        )

        # Obter todas as avaliações
        reviews = driver.find_elements(By.CLASS_NAME, "section-review-content")

        # Extrair o texto das avaliações
        for review in reviews:
            author_name = review.find_element(By.CLASS_NAME, "section-review-title").text
            rating = review.find_element(By.CLASS_NAME, "section-review-stars").get_attribute("aria-label")
            review_text = review.find_element(By.CLASS_NAME, "section-review-text").text

            print(f"Author: {author_name}\nRating: {rating}\nReview: {review_text}\n")

    except Exception as e:
        print(f"Erro durante o scraping: {e}")

    finally:
        # Fechar o navegador após a conclusão do scraping
        driver.quit()

# Exemplo de uso:
if __name__ == "__main__":
    local_url = "https://www.google.com.br/maps/search/restaurants"
    scrape_google_maps_reviews(local_url)
