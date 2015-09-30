import requests
from bs4 import BeautifulSoup

search = 'http://www.google.com/#q=taco'

responseObj = requests.get(search)
soup = BeautifulSoup(responseObj.content) # valid
data = soup.find_all('h3',{'class': 'r'})
# data is an empty list, but the URL has an <h3 class='r'>

soup = BeautifulSoup(responseObj.text) # valid
data = soup.select('.r a')
# same problem, data is still empty... 
