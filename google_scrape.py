import requests
from bs4 import BeautifulSoup
from ghost import Ghost

search = 'http://www.google.com/#q=taco'
ghost = Ghost()

with ghost.start() as session:
    page, resources = session.open(search)
    session.wait_for_selector('h3.r')
  
    soup = BeautifulSoup(page)
    data = soup.find_all('h3',{'class':'r'})
