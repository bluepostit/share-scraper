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
    print(shares)
    shares = {
        'searchTerm': search_term,
        'resultsCount': sum(list(shares.values())),
        'brands': list(shares.keys()),
        'shares': [
            {
                'provider': 'lazada',
                'shares': list(shares.values())
            },
            # {
            #     'provider': 'second provider',
            #     'shares': list(shares.values())
            # }
        ]
    }
    return jsonify(shares)
