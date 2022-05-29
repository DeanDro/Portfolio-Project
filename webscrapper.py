from bs4 import BeautifulSoup
import requests

wait_for_input = True


while wait_for_input:

    f = open('./microservices/text_files/webscraper.txt', 'r')
    content = f.readline() # Read from text files the city we want to scrape

    f.close()

    if content != '':

        # Make a request to WikiPedia
        city_page = requests.get('https://en.wikipedia.org/wiki/' + content).text
        soup = BeautifulSoup(city_page, 'lxml')
        city_details = soup.find('div', class_='mw-parser-output')

        parag = city_details.find_all('p')

        # Collect only the first 3 paragraphs from WikiPedia page
        result = parag[0].text + parag[1].text + parag[2].text
        
        p = open('./microservices/text_files/webscraper_result.txt', 'w', encoding='utf8')
        p.write(str(result))
        p.close()
