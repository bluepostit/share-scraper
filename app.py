import random
from flask import Flask
# from scraper.browser import ScraperBrowser
from scraper.scraper.lazada_simple import LazadaSimpleScraper

app = Flask(__name__)
app.config.from_pyfile('app.cfg')


@app.route('/')
def main():
    return '<div>Click <a href="/test/">here</a> to test the scraper</div>'


@app.route('/test/')
def test_scraper():
    scraper_api_key = app.config['SCRAPERAPI_KEY']
    search_terms = ['ipod', 'handbag', 'Webcam logitech', 'Mp3 player']
    search_term = random.choice(search_terms)
    scraper = LazadaSimpleScraper().set_scraper_api_key(scraper_api_key)
    results = scraper.get_brand_share(search_term, 100)

    print(f"Found {len(results)} results.")

    return str(results)

