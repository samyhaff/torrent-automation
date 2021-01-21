from bs4 import BeautifulSoup
import requests

source = requests.get("https://nyaa.si/?f=0&c=0_0&q=full+metal+alchemist+brotherhood&s=downloads&o=desc").text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find('tbody')
tr = tbody.find('tr')
for tr in tbody.find_all('tr'):
    tds = tr.find_all('td')
    # print(tds[1].prettify())
    title = tds[1].find_all('a')[-1]
    print(title.text)
