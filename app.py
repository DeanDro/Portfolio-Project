from flask import Flask, render_template, request
import time

app = Flask(__name__)


def collect_wikipedia_data(keyword):
    """
    Takes as a parameter a keyword string. Writes the keyword to webscraper.txt file for the webscraper to collect
    and scrape WikiPedia for this keyword. The result will be written in the webscraper_result.txt file for this
    function to collect and return.
    """

    f = open('microservices/text_files/webscraper.txt', 'w')
    f.write(keyword)
    f.close()

    time.sleep(3)

    p = open('microservices/text_files/webscraper_result.txt', 'r', encoding='utf8')
    content = p.readlines()[2]  # We select the 3 element in the list to avoid the language descriptions in the front
    p.close()

    if content !='':
        f = open('microservices/text_files/webscraper.txt', 'w')
        f.write('')
        f.close()

        p = open('microservices/text_files/webscraper_result.txt', 'w')
        p.write('')
        p.close()

    return content

def find_distance_destinations(city1, city2):
    """
    Gets two strings as parameters with the two locations we want to visit. It will format the query and write the text
    in the file distance_scrap.txt and wait for 5 sec. From there the google_scraper.py microservice will read the query and send a
    request to google to get the distance. Then it will write the result back to the distance_scrap.txt file, from which this
    function will read the result.
    """

    f = open('microservices/text_files/distance_scrap.txt', 'w')
    query = str(city1 +'-' + city2)
    f.write(query)
    f.close()

    time.sleep(5)  # Changed from 5 seconds before

    f = open('microservices/text_files/distance_result.txt', 'r', encoding='utf8')
    content = f.readline()
    f.close()

    time.sleep(2)
    f = open('microservices/text_files/distance_result.txt', 'w')
    f.write('')
    f.close()

    return content.split('-')

def quotes_request():
    """
    Sends a request to the microservice wikiquote and it returns a quote
    from the WikiQuote page.
    """

    f = open('microservices/text_files/quote.txt', 'w')
    f.write('Quote')
    f.close()

    time.sleep(2)

    f = open('microservices/text_files/quote_result.txt', 'r')
    content = f.readlines()
    f.close()

    return str(content[0])

def sort_list(destinations_list):
    """
    This is the method to run the microservice created by Nicolas Fong for sorting a
    list of strings.
    """

    # Write the list to be sorted in the data.txt file
    p = open('./Microservice_Nicolas_Fong/data.txt', 'w')

    for i in range(len(destinations_list)):
        p.write(destinations_list[i])
        p.write('\n')
    p.close()

    f = open('./Microservice_Nicolas_Fong/commands.txt', 'w')
    f.write('sort')
    f.close()

    # wait for the list to sort
    time.sleep(5)

    # Collect sorted list
    sorted_list = []
    with open('./Microservice_Nicolas_Fong/data.txt', 'r+') as f:
        for line in f:
            locations = line[:-1]
            sorted_list.append(str(locations))
    f.close()

    return sorted_list

def get_image_url(city):
    """
    Uses microservice by Dan Shatil to returns the address of an image from pixabay. Get's a string with the location we want to
    search for and searches for an image in Pixabay with that value.
    """
    f = open('Microservice_Dan_Shatil/image.txt', 'w')
    f.write(city)
    f.close()

    time.sleep(1)

    f = open('Microservice_Dan_Shatil/image.txt', 'r', encoding='utf8')
    img_address = f.readlines()
    f.close()

    return img_address

def convert_time_distance(distance_details):
    """
    Helper method that takes the distance and the time it will take to
    complete the route, converts it from string to float and returns the
    revised array.
    """
    new_array = []
    new_array.append(float(distance_details[0]))
    new_array.append(float(distance_details[1]))

    return new_array

@app.route('/')
def index():

    # Get an inspirational quote on the homepage
    quote = quotes_request()

    return render_template('index.html', quote=quote)

@app.route('/mountainview', methods=['GET', 'POST'])
def mountainview():
    if request.method == 'GET':

        # Use Nicolas Fong microservice to sort the list of destinations in an alphabetical order.
        destinations_list = ['Rome_Florence', 'Lisbon_Barcelona', 'Dusseldorf_Amsterdam', 'Paris_Marseille', 'London_Cardiff']
        sorted_list = sort_list(destinations_list)

        return render_template('mountainRoutes.html', destinations=sorted_list)
    else:
        # Get path selection
        get_arg = request.form['trail']
        if get_arg == 'Rome_Florence':
            cities = ['Rome', 'Florence']
        elif get_arg == 'Lisbon_Barcelona':
            cities = ['Lisbon', 'Barcelona']
        elif get_arg == 'Dusseldorf_Amsterdam':
            cities = ['Dusseldorf', 'Amsterdam']
        elif get_arg == 'Paris_Marseille':
            cities = ['Paris', 'Marseille']
        else:
            cities = ['London', 'Cardiff']

        #Scrape information for each city
        city1 = collect_wikipedia_data(cities[0])
        city2 = collect_wikipedia_data(cities[1])

        #Call microservice distance_api.py to get the distance between the two cities
        distance = find_distance_destinations(cities[0], cities[1])

        # Use microservice by Dan Shatil to retrieve an image from Pixabay
        city1_img = get_image_url(cities[0])
        city1_details = cities[0]

        time.sleep(2)

        # Use microservice by Dan Shatil to retrieve an image from Pixabay
        city2_img = get_image_url(cities[1])
        city2_details = cities[1]

        # Details about the trip
        trip_info = convert_time_distance(distance)

        time.sleep(4)

        return render_template('routePage.html', city1_img=city1_img, city1=city1, city2=city2, cities=cities,
                                distance=trip_info[0], duration=trip_info[1], city1_details=city1_details,
                                city2_details=city2_details, city2_img=city2_img)

@app.route('/seaside', methods=['GET', 'POST'])
def seaside():
    if request.method == 'GET':

         # Use Nicolas Fong microservice to sort the list of destinations in an alphabetical order.
        destinations_list = ['Marseille_Montpellier', 'Hamburg_Copenhagen', 'Valencia_Barcelona',
                            'Gothenburg_Malmo', 'Lisbon_Porto']
        sorted_list = sort_list(destinations_list)
        return render_template('seasideRoutes.html', destinations=sorted_list)
    else:

        # Get path selection
        get_arg = request.form['trail']
        if get_arg == 'Marseille_Montpellier':
            cities = ['Marseille', 'Montpellier']
        elif get_arg == 'Hamburg_Copenhagen':
            cities = ['Hamburg', 'Copenhagen']
        elif get_arg == 'Valencia_Barcelona':
            cities = ['Valencia', 'Barcelona']
        elif get_arg == 'Gothenburg_Malmo':
            cities = ['Gothenburg', 'Malmo']
        else:
            cities = ['Lisbon', 'Porto']

        # Scrape information for each city
        city1 = collect_wikipedia_data(cities[0])
        city2 = collect_wikipedia_data(cities[1])

        # Use microservice by Dan Shatil to retrieve city images from Pixabay
        city1_img = get_image_url(cities[0])
        city1_details = cities[0]

        time.sleep(2)

        # Uses microservice by Dan Shatil to retrieve city images from Pixabay
        city2_img = get_image_url(cities[1])
        city2_details = cities[1]

        # call microservice distance_api.py to get distance and duration of a ride
        distance = find_distance_destinations(cities[0], cities[1])

        # Details about the trip
        trip_info = convert_time_distance(distance)

        return render_template('routePage.html', city1_img=city1_img, city1=city1, city2=city2, cities=cities,
                                distance=trip_info[0], duration=trip_info[1], city1_details=city1_details,
                                city2_details=city2_details, city2_img=city2_img)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/disclosure')
def disclosure():
    return render_template('disclosure.html')


if __name__ == '__main__':
    app.run(debug=True)
