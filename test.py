from bs4 import BeautifulSoup
import requests

response = requests.get('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html').text
soup = BeautifulSoup(response, 'html.parser')

upc = soup.select_one(".table tr:nth-child(1) > td")
# content_inner > article > table > tbody > tr:nth-child(1) > td


title = soup.select_one('h1')


price_incl_tax = soup.select_one(".table tr:nth-child(4) > td")


price_exl_tax = soup.select_one(".table tr:nth-child(3) > td")


number_available = soup.select_one(".table tr:nth-child(6) > td")

# table >  tr:nth-child(6) > td


product_description = soup.select_one("article > p".strip())


category = soup.select_one("li:nth-child(3) >a ")

image_url = soup.find("img")
print(image_url)

#product_gallery > div > div > div > img

review_rating = soup.find("i", class_="icon-star")


# content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating.Two > i:nth-child(2)

# image_url = soup.find('img')
