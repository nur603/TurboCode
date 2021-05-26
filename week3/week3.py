import requests
from bs4 import BeautifulSoup
url = 'https://kolesa.kz/cars/sedan/almaty/?auto-sweel=1&auto-car-order=1&year[from]=2010&price[from]=2+000+000&price[to]=7+000+000'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'lxml')
ids = soup.find_all('a', class_='ddl_product_link')
print(ids)
