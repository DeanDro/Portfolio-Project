from bs4 import BeautifulSoup
import requests
import random
import time

search_quote = True

while search_quote:

    f = open('./microservices/text_files/quote.txt', 'r')
    content = f.readline()
    f.close()

    if content != '':

        # Make a request to WikiQuote page.
        quote_pages = requests.get('https://en.wikiquote.org/wiki/Wikiquote:Quotes_of_the_Year').text
        quotes = BeautifulSoup(quote_pages, 'lxml')

        # Select a random number
        rant = random.randint(0, 20)

        quotes_segment = quotes.find('div', class_='mw-parser-output')
        quotes_list = quotes_segment.find_all('li')

        # Select a random quote from the page
        quote = str(quotes_list[rant].text)
        
        f = open('./microservices/text_files/quote_result.txt', 'w')
        f.write(str(quote))
        f.close()

        time.sleep(2)

        f = open('./microservices/text_files/quote.txt', 'w')
        f.write('')
        f.close()
