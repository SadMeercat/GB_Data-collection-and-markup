from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv

url = 'https://4pda.to/reviews/smartphones/'

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(5)  # Задержка для полной загрузки страницы

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

articles = soup.find_all(attrs={"itemprop": "name"})

with open('4pda_smartphones_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])
    
    # Извлечение заголовков
    for article in articles:
        headline = article.get_text()
        writer.writerow([headline])

print("Данные успешно извлечены и сохранены")
