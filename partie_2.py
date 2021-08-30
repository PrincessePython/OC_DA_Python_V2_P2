from bs4 import BeautifulSoup
import requests

cat_url = 'https://books.toscrape.com/catalogue/category/books/humor_30/index.html'
response = requests.get(cat_url)
soup = BeautifulSoup(response.content, 'html.parser')

for books in soup.find_all("h3"):
    print(f'--> ', {books}, end ='\n'*2)
    

#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a





















"""
def scrap_cat(cat_url):

    response = requests.get(cat_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return{


        
    }

#default > div > div > div > div > section > div:nth-child(2) > ol


cat = scrap_cat('https://books.toscrape.com/catalogue/category/books/humor_30/index.html')
print(cat)
"""