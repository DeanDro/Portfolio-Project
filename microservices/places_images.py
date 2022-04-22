import requests
import json

images_url = 'https://pixabay.com/api/'

key_file = open('C:/Users/Konstantinos/Desktop/Oregon State University/CS 361/images_key.txt', 'r')
img_key = key_file.read()
key_file.close()

def get_image_location(city):
    """
    Get a city as a string argument and returns a url to an image from pixabay with the location we asked for. 
    """
    request_url = images_url + '?key=' + img_key + '&q=' + city
    img_request = requests.get(request_url).text
    img_data = json.loads(img_request)
    top_img = img_data['hits'][0]['pageURL']
    return top_img
