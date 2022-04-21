from bs4 import BeautifulSoup
import requests

def get_genoa_monaco():
    """
    Returns the wikepedia page for Genoa
    """
    genoa_page = requests.get('https://en.wikipedia.org/wiki/Genoa').text
    soup = BeautifulSoup(genoa_page, 'lxml')
    city_details = soup.find('div', class_='mw-parser-output')
    parag = city_details.find_all('p')

    return parag

