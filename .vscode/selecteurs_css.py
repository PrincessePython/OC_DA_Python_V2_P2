from bs4 import BeautifulSoup
import requests

response = requests.get('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html').text
soup = BeautifulSoup(response, 'html.parser')

image_url = soup.select(".carousel > div > div > div > img")

review_raiting = soup.select_one('div.col-sm-6.product_main > p.star-rating.Two > i:nth-child(2)')
print(review_raiting)

#content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating.Two > i:nth-child(2)

#product_gallery > div > div > div > img