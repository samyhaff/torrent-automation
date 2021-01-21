from bs4 import BeautifulSoup
import requests
import sys

query = sys.argv[1].replace(" ", "+")
source = requests.get("https://nyaa.si/?f=0&c=0_0&q=" + query +"&s=downloads&o=desc").text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find('tbody')
tr = tbody.find('tr')
for i, tr in enumerate(tbody.find_all('tr')):
    tds = tr.find_all('td')
    title = tds[1].find_all('a')[-1].text
    link = tds[2].find('a').get("href")
    size = tds[3].text
    seeds = tds[5].text
    print(str(i) + " " + title + " " + size + " " + seeds + " " + link)
