import requests
import json

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
    'Dessuldrof': 'Q1718',
    'Hamburg' : 'Q1055',
    'Copenhagen': 'Q1748'
}


def get_distance_between_cities(city1, city2):
    """
    Takes the name of the cities as a string, looks for the cities in the cities_dictionary to get their wikidata id and
    makes a request to the geo-db api to get he distance between them in km. It returns an array with value at index 0 
    the distance in km and in index 1 the average time it will take an average biker to complete the distance.
    """
    try :
        city_code1 = cities_dictionary[city1]
        city_code2 = cities_dictionary[city2]

        querystring1 = {"distanceUnit":"KM","toCityId":city_code1}
        response1 = json.loads(requests.request("GET", distance_url, headers=headers, params=querystring1).text)

        querystring2 = {"distanceUnit":"KM","toCityId":city_code2}
        response2 = json.loads(requests.request("GET", distance_url, headers=headers, params=querystring2).text)
        
        distance_km = round(abs(float(response1['data']) - float(response2['data'])),2)
        average_time = str(round(float((distance_km / 25) * 60),2)) + ' hours'
        result = [distance_km, average_time]
        
        return result

    except :
        return ['An error occured in the calculation', 'An error occured in the calculation']
    
print(get_distance_between_cities('Amsterdam', 'Genoa'))