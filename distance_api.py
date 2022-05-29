import requests
import json
import time

"""
Utilizing the GeoDB API to return the distance between two cities
"""

distance_finder = True

while distance_finder:

    f = open('./microservices/text_files/distance_scrap.txt', 'r')
    content = f.readline()
    f.close()


    if content != '':

        cities = content.split('-')

        # URL for getting distance between endpoints
        distance_url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60/distance'

        # Login Key
        key_file = open('C:/Users/Konstantinos/Desktop/Oregon State University/CS 361/geo_key.txt', 'r')
        geo_key = key_file.read()
        key_file.close()

        # Connection details
        headers = {
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
            "X-RapidAPI-Key": geo_key
        }

        # Wikidata ids for cities in the list of options
        cities_dictionary = {
            'Genoa': 'Q1449',
            'Monaco City': 'Q55115',
            'Barcelona': 'Q1492',
            'Valencia': 'Q8818',
            'Amsterdam': 'Q727',
            'Dusseldorf': 'Q1718',
            'Hamburg' : 'Q1055',
            'Copenhagen': 'Q1748',
            'Rome': 'Q220',
            'Florence': 'Q2044',
            'Lisbon': 'Q597',
            'Marseille' : 'Q23482',
            'Montpellier': 'Q6441',
            'Gothenburg': 'Q25287',
            'Malmo': 'Q2211',
            'Porto': 'Q33707919',
            'Paris': 'Q90',
            'London': 'Q84',
            'Cardiff': 'Q10690'
        }

        city1 = cities_dictionary[cities[0]]
        city2 = cities_dictionary[cities[1]]

        # Make a reqeuest to geo-db API for the location of the first city
        querystring1 = {"distanceUnit":"KM","toCityId":city1}
        response1 = json.loads(requests.request("GET", distance_url, headers=headers, params=querystring1).text)
        distance1 = response1.get('data')

        time.sleep(2) # Wait for 2sec due to cap on API requests per sec

        # Make a request to geo-db API for the second city
        querystring2 = {"distanceUnit":"KM","toCityId":city2}
        response2 = json.loads(requests.request("GET", distance_url, headers=headers, params=querystring2).text)
        distance2 = response2.get('data')

        # Calculate the distance between the 2 cities and estimated time.
        # Average speed used for time calculation: 20km/h
        distance_km = round(abs(float(str(distance1)) - float(str(distance2))),2)
        average_time = str(round(float((distance_km / 20)),2))
        result = str(distance_km) + '-' + str(average_time)

        p = open('./microservices/text_files/distance_result.txt', 'w')
        p.write(result)
        p.close()

        time.sleep(2)

        p = open('./microservices/text_files/distance_scrap.txt', 'w')
        p.write('')
        p.close()
