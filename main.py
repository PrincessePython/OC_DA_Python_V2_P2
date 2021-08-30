from bs4 import BeautifulSoup
import requests


def scrap_book(page_url):

    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return {
        "upc": soup.select_one('.table tr:nth-child(1) > td'),
        "title": soup.select_one('h1'),
        "price_incl_tax": soup.select_one(".table tr:nth-child(4) > td"),
        "price_exl_tax": soup.select_one(".table tr:nth-child(3) > td"),
        "number_available": soup.select_one(".table tr:nth-child(6) > td"),
        "product_description": soup.select_one("article > p".strip()),
        "product_category": soup.select_one("li:nth-child(3) >a "),
        "review_rating": soup.find("i", class_="icon-star"),
        "image_url": soup.select(".carousel > div > div > div > img")
        }


book = scrap_book('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')


for name, value in book.items():
    print(name, ' : ', value)
