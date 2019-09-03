class SimpleScraper:
    def get_brand_share(self, search_term, results_limit):
        pass

    def set_scraper_api_key(self, key):
        self.scraper_api_key = key
        return self

    def _get_brands_as_shares(self, brands):
        shares = {}
        for brand in brands:
            if brand in shares:
                shares[brand] += 1
            else:
                shares[brand] = 1
        return shares

class Scraper(SimpleScraper):
    def __init__(self, browser):
        self.browser = browser
