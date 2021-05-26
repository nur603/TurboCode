import requests
from bs4 import BeautifulSoup
url = 'https://kolesa.kz/cars/sedan/almaty/?mark-country=12&auto-sweel=1&auto-car-order=1&year[from]=2010&year[to]=2012'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
kolesa = soup.find_all('span',class_='a-el-info-title')
for i in kolesa:
	bsoup = i.find('a',class_='list-link ddl_product_link')
	link = bsoup.get('data-product-id')
	url = str('https://kolesa.kz/a/show/') + link
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	cheaper = soup.find('span', class_='cheaper')
	brand = soup.find('span', itemprop='brand').text.strip()
	name = soup.find( 'span', itemprop='name').text.strip()
	if cheaper != None:
		cheaper = soup.find('span', class_='cheaper').text.strip()
		print(f'{brand} {name} {cheaper}')


