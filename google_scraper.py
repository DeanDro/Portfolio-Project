import requests
from bs4 import BeautifulSoup

distance_finder = True

while distance_finder:

    f = open('./microservices/text_files/distance_scrap.txt', 'r')
    content = f.readline()
    f.close()

    if content != '':

        distance_locations = requests.get('https://google.com/search?q=' + content).text
        soup = BeautifulSoup(distance_locations, 'lxml')
        distances = soup.find('div', class_='BbbuR uc9Qxb uE1RRc')

        print(soup)