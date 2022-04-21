from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import microservices.web_scraping as scrape

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

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
        get_arg = request.form['trail']
        if get_arg == 'Genoa_Monaco':
            wiki_content = scrape.get_genoa_monaco()
            result = str(wiki_content[1]) + str(wiki_content[2]) + str(wiki_content[3])
            return result
        else:
            return str(get_arg)

@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)