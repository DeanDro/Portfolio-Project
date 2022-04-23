import requests
import json
import io
from PIL import Image

images_url = 'https://pixabay.com/api/'

key_file = open('C:/Users/Konstantinos/Desktop/Oregon State University/CS 361/images_key.txt', 'r')
img_key = key_file.read()
key_file.close()

def get_image_location(city):
    """
    Get a city as a string argument and returns a url to an image from pixabay with the location we asked for. 
    """
    request_url = images_url + '?key=' + img_key + '&q=' + city
    img_request = requests.get(request_url)
    img_data = json.loads(img_request.text)
    top5_imgs = []
    try:
        for i in range(3):
            top_img = img_data['hits'][i]['webformatURL']
            top5_imgs[i] = str(top_img)
    except:
        top5_imgs = [str(img_data['hits'][0]['webformatURL'])]

    return top5_imgs
