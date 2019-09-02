import random
from flask import Flask, current_app, request
from flask import jsonify
# from scraper.browser import ScraperBrowser
from scraper.scraper.lazada_simple import LazadaSimpleScraper

app = Flask(__name__)
app.config.from_pyfile('app.cfg')


@app.route('/')
def main():
    return current_app.send_static_file('index.html')


@app.route('/search/')
def search():
    search_term = request.args.get('term')
    scraper_api_key = app.config['SCRAPERAPI_KEY']
    scraper = LazadaSimpleScraper().set_scraper_api_key(scraper_api_key)
    shares = scraper.get_brand_shares(search_term, 100)
    return jsonify(shares)


@app.route('/test/')
def test_scraper():
    scraper_api_key = app.config['SCRAPERAPI_KEY']
    search_terms = ['ipod', 'handbag', 'Webcam logitech', 'Mp3 player']
    search_term = random.choice(search_terms)
    scraper = LazadaSimpleScraper().set_scraper_api_key(scraper_api_key)
    shares = scraper.get_brand_shares(search_term, 100)
    return jsonify(shares)


@app.route('/collect/')
def test_collect():
    f = open('mp3-player-brands-simple.txt')
    brands = f.readlines()
    print(f"total brands: {len(brands)}")
    shares = {}
    for brand in brands:
        if brand in shares:
            shares[brand] += 1
        else:
            shares[brand] = 1
    print(shares)
    return jsonify(shares)
