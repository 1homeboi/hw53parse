from bs4 import BeautifulSoup
import requests
import json

link = "https://www.lamoda.kz/c/17/shoes-men/?brand_group=1&sitelink=topmenuM&l=2"
page = requests.get(link)

soup = BeautifulSoup(page.text, "html.parser")

div = soup.find_all ("div", class_= "x-product-card-description")
if not div:
    raise Exception("Product couldnt be found")
result = []
for s in div:
    result.append (s.text.strip().replace("\n",""))

with open('data.json', 'w') as json_file:
    json.dump(result, json_file)