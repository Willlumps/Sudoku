from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

url = 'https://www.websudoku.com/'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="puzzle_container", style="position:relative;")

print(results)






