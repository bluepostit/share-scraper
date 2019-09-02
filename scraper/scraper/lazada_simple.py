import random
import re
import requests
from .base import SimpleScraper

class LazadaSimpleScraper(SimpleScraper):
    SEARCH_URL = "https://www.lazada.vn/catalog/?q=##SEARCH_TERM##&_keyori=ss" \
        + "&from=input&spm=a2o4n.home.search.go.1905e18214cAJy"

    USER_AGENTS = [
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 ' \
            + '(KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'
    ]

    def get_brand_share(self, search_term, results_limit):
        url = self.SEARCH_URL.replace('##SEARCH_TERM##', search_term)
        with requests.session() as session:
            headers = {
                'User-Agent': random.choice(self.USER_AGENTS)
            }
            page = session.get(url, headers=headers)
            print(page)
            brands = self.get_brands(page.text)
            return brands

    def get_brands(self, html):
        print(html)
        regex = re.compile('"brandName":"([^"]+)"')
        matches = re.findall(regex, html)
        return matches
