from msilib.schema import Error
import requests
import json
import time


website_url = 'https://pixabay.com/api/'

# key_file = open('./text_files/key.txt', 'r')
# api_key = key_file.read()
# key_file.close()

# API Key is hardcoded for now, will be changed to a user-specific key
key_file = open('C:/Users/Konstantinos/Desktop/Oregon State University/CS 361/images_key.txt', 'r')
api_key = key_file.read()
key_file.close()

def get_image_url(city, large=False):
    """
    takes a string city, returns url of image
    large parameter toggles large or standard size image
    """
    request_url = website_url + '?key=' + api_key + '&q=' + city
    img_request = requests.get(request_url)
    img_data = json.loads(img_request.text)
    try:
        top_result = img_data['hits'][0][('webformatURL', 'largeImageURL') [large]]
    except:
        raise Error

    return top_result


while True:

    f = open('Microservice_Dan_Shatil/image.txt', 'r', encoding='utf8')
    content = f.readline()
    f.close()

    if content != '':

        result = get_image_url(content)

        f = open('Microservice_Dan_Shatil/image.txt', 'w')
        f.write(result)
        f.close()

        time.sleep(2)

        f = open('Microservice_Dan_Shatil/image.txt', 'w')
        f.write('')
        f.close()

