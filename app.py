from flask import Flask, render_template, request
import microservices.web_scraping as scrape
import microservices.google_maps as maps
import microservices.places_images as place_img
import time

app = Flask(__name__)

routes_distance_duration = {
    'Rome_Florence': ['296km', '17hrs'],
    'Lisbon_Barcelona': ['1,277km', '66hrs'],
    'Dusseldorf_Amsterdam' : ['225km', '12hrs'],
    'Paris_Marseille': ['806km', '42hrs'],
    'London_Cardiff': ['291km', '16hrs'],
    'Marseille_Montpellier': ['170km', '9hrs'],
    'Hamburg_Copenhagen': ['336km', '18hrs'],
    'Valencia_Barcelona': ['369km', '19hrs'],
    'Gothenburg_Malmo': ['320km', '17hrs'],
    'Lisbon_Porto': ['341km', '18hrs']
}

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

    time.sleep(5)

    f = open('microservices/text_files/distance_scrap.txt', 'r', encoding='utf8')
    content = f.readline()
    f.close()

    return content.split('-')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mountainview', methods=['GET', 'POST'])
def mountainview():
    if request.method == 'GET':
        return render_template('mountainRoutes.html')
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

        #Call microservice google_scraper.py to get the distance between the two cities 
        distance = find_distance_destinations(cities[0], cities[1])

        # get image of the destinations - starting point
        city1_img = place_img.get_image_location(cities[0])
        city1_details = cities[0]
        city2_img = place_img.get_image_location(cities[1])
        city2_details = cities[1]
            
        # Details about the trip
        #trip_info = maps.get_distance_between_cities(cities[0], cities[1])
        trip_info = distance

        return render_template('routePage.html', city1_img=city1_img, city1=city1, city2=city2, cities=cities, 
                                distance=trip_info[0], duration=trip_info[1], city1_details=city1_details,
                                city2_details=city2_details, city2_img=city2_img)

@app.route('/seaside', methods=['GET', 'POST'])
def seaside():
    if request.method == 'GET':
        return render_template('seasideRoutes.html')
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

        # get image of the destinations - starting point
        city1_img = place_img.get_image_location(cities[0])
        city1_details = cities[0]
        city2_img = place_img.get_image_location(cities[1])
        city2_details = cities[1]
            
        # Details about the trip
        #trip_info = maps.get_distance_between_cities(cities[0], cities[1])
        trip_info = routes_distance_duration[get_arg]

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