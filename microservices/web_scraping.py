from bs4 import BeautifulSoup
import requests

def get_cities_details(cities):
    """
    Returns the wikepedia page for Genoa
    """
    city_page = requests.get('https://en.wikipedia.org/wiki/' + cities).text
    soup = BeautifulSoup(city_page, 'lxml')
    city_details = soup.find('div', class_='mw-parser-output')
    parag = city_details.find_all('p')

    result = parag[0].text + parag[1].text + parag[2].text

    return result
