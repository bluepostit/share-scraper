import random
from flask import Flask
from scraper.browser import ScraperBrowser
from scraper.scraper.lazada import LazadaScraper

app = Flask(__name__)

@app.route('/')
def main():
    return '<div>Click <a href="/test/">here</a> to test the scraper</div>'

@app.route('/test/')
def test_scraper():
    search_terms = ['ipod', 'handbag', 'Webcam logitech', 'Mp3 player']
    search_term = random.choice(search_terms)
    browser = ScraperBrowser(headless=False)
    scraper = LazadaScraper(browser)
    results = scraper.get_brand_share(search_term, 100)

    # home_page = lazada.HomePage(browser)
    # home_page.load().search(search_term)

    # search_page = lazada.SearchPage(browser)
    # results = search_page.get_results()

    # for result in results[0:4]:
    #     product_page = lazada.ProductPage(browser)
    #     product_page.open_new_tab().load(result)
    #     brand = product_page.get_brand()
    #     print(f"Brand: {brand}")
    #     product_page.close_tab()

    browser.quit()

    return str(results)

    # return f"Found {len(results)} results."
