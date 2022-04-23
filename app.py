from flask import Flask, render_template, request
import microservices.web_scraping as scrape
import microservices.google_maps as maps
import microservices.places_images as place_img

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mountainview', methods=['GET', 'POST'])
def mountainview():
    if request.method == 'GET':
        return render_template('mountainRoutes.html')
    else:
        get_arg = request.form['trail']
        return get_arg

@app.route('/seaside', methods=['GET', 'POST'])
def seaside():
    if request.method == 'GET':
        return render_template('seasideRoutes.html')
    else:

        # Get path selection
        get_arg = request.form['trail']
        if get_arg == 'Genoa_Monaco_City':
            cities = ['Genoa', 'Monaco City']
        elif get_arg == 'Hamburg_Copenhagen':
            cities = ['Hamburg', 'Copenhagen']
        else:
            cities = ['Valencia', 'Barcelona']

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
        trip_info = ['Unavailable', 'Unavailable']

        return render_template('routePage.html', city1_img=city1_img, city1=city1, city2=city2, cities=cities, 
                                distance=trip_info[0], duration=trip_info[1], city1_details=city1_details,
                                city2_details=city2_details, city2_img=city2_img)

@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)