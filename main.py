from bs4 import BeautifulSoup
import requests


def scrap_book(page_url):
    response = requests.get(page_url).text
    soup = BeautifulSoup(response, 'html.parser')
    return {
        "upc": soup.select_one('.table tr:nth-child(1) > td').text
    }


book = scrap_book('https://books.toscrape.com/catalogue/birdsong-a-story-in-pictures_975/index.html')
1+1

