from bs4 import BeautifulSoup
import requests

query = "full metal alchemist brotherhood".replace(" ", "+")
source = requests.get("https://nyaa.si/?f=0&c=0_0&q=" + query +"&s=downloads&o=desc").text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find('tbody')
tr = tbody.find('tr')
for tr in tbody.find_all('tr'):
    tds = tr.find_all('td')
    title = tds[1].find_all('a')[-1]
    link = tds[2].find('a')
    size = tds[3].text
    seeds = tds[5].text
