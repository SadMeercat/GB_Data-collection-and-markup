import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import json

url = "https://books.toscrape.com"
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

ua = UserAgent()

headers = {
    "User-Agent": ua.random
}

session = requests.Session()

page_num = 1
books = []

while True:
    print(f"page num: {page_num}")
    response = session.get(url=base_url.format(page_num), headers=headers)

    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for row in rows:
        book = {}

        title_info = row.find("h3").find("a")
        tmp_url = url + "/catalogue/" + title_info.get("href")
        book['title'] = title_info.get("title")
        book["price"] = row.find("p", {"class": "price_color"}).getText()[1:]

        if "In stock" in row.find("p", {"class": "instock availability"}).getText().strip():
            tmp_response = session.get(url=tmp_url)
            tmp_soup = BeautifulSoup(tmp_response.text, "html.parser")

            stock = int(re.findall(r'\d+', tmp_soup.find("p", {"class": "instock availability"}).getText())[0])
        else:
            stock = "Out of stock"
        book["stock"] = stock

        books.append(book)
    page_num += 1
with open("books.json", "w") as file:
    json.dump(books, file, indent=4)