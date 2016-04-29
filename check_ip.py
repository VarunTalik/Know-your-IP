import requests
from bs4 import BeautifulSoup

url = "http://www.whatsmyip.org"

for x in range(0,5):
	response = requests.get(url).content

	soup = BeautifulSoup(response,'lxml')
	result = soup.findAll('h1')

	for each in result:
		print each.text
		break