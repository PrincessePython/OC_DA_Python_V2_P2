from bs4 import BeautifulSoup
import requests

def scrap_cat(cat_url):

    response = requests.get(cat_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return{


        
    }


cat = scrap_cat('https://books.toscrape.com/catalogue/category/books/humor_30/index.html')
print(cat)