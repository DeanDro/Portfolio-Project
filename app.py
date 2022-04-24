from flask import Flask, render_template, request
import microservices.web_scraping as scrape
import microservices.google_maps as maps
import microservices.places_images as place_img

app = Flask(__name__)

routes_distance_duration = {
    'Rome_Florence': ['296km', '17hrs'],
    'Lisbon_Barcelona': ['1,277km', '66hrs'],
    'Dusseldorf_Amsterdam' : ['225km', '12hrs'],
    'Paris_Marseille': ['806km', '42hrs'],
    'London_Cardiff': ['291km', '16hrs'],
    'Nice_Montpellier': ['348km', '19hrs'],
    'Hamburg_Copenhagen': ['336km', '18hrs'],
    'Valencia_Barcelona': ['369km', '19hrs'],
    'Gothenburg_Malmo': ['320km', '17hrs'],
    'Lisbon_Porto': ['341km', '18hrs']
}

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
        city1 = scrape.get_cities_details(cities[0])
        city2 = scrape.get_cities_details(cities[1])

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

@app.route('/seaside', methods=['GET', 'POST'])
def seaside():
    if request.method == 'GET':
        return render_template('seasideRoutes.html')
    else:

        # Get path selection
        get_arg = request.form['trail']
        if get_arg == 'Nice_Montpellier':
            cities = ['Nice', 'Montpellier']
        elif get_arg == 'Hamburg_Copenhagen':
            cities = ['Hamburg', 'Copenhagen']
        elif get_arg == 'Valencia_Barcelona':
            cities = ['Valencia', 'Barcelona']
        elif get_arg == 'Gothenburg_Malmo':
            cities = ['Gothenburg', 'Malmo']
        else:
            cities = ['Lisbon', 'Porto']

        # Scrape information for each city
        city1 = scrape.get_cities_details(cities[0])
        city2 = scrape.get_cities_details(cities[1])

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