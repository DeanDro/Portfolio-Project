from bs4 import BeautifulSoup
import requests

#wait_for_input = True


#while wait_for_input:

    #f = open('text_files/webscraper.txt', 'r')
    #content = f.readline()

    #f.close()

    #if content != '':

        #city_page = requests.get('https://en.wikipedia.org/wiki/' + content).text
        #soup = BeautifulSoup(city_page, 'lxml')
        #city_details = soup.find('div', class_='mw-parser-output')
        #parag = city_details.find_all('p')

        #result = parag[0].text + parag[1].text + parag[2].text

        #p = open('text_files/webscraper_result.txt', 'w')
        #p.write(result)
        #p.close()




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
