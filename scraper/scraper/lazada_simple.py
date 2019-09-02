from math import ceil
import random
import re
import requests
from .base import SimpleScraper

class LazadaSimpleScraper(SimpleScraper):
    RESULTS_PER_PAGE = 40

    SEARCH_URL = "https://www.lazada.vn/catalog/?q=##SEARCH_TERM##" \
        + "&_keyori=ss&from=input&spm=a2o4n.home.search.go.1905e18214cAJy"

    USER_AGENTS = [
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 '
        + '(KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'
    ]

    def get_brand_share(self, search_term, results_limit):
        base_url = self.SEARCH_URL.replace('##SEARCH_TERM##', search_term)
        amt_pages = ceil(results_limit / self.RESULTS_PER_PAGE)
        print(f"pages to load: {amt_pages}")

        brands = []
        with requests.session() as session:
            headers = {
                'User-Agent': random.choice(self.USER_AGENTS)
            }
            # First page
            print("loading first page")
            print(base_url)
            page = session.get(base_url, headers=headers)
            brands += self.get_brands(page.text)
            f = open(f"{search_term.replace(' ', '_')}-out.html", 'w')
            f.write(page.text)

            # Additional pages
            for i in range(1, amt_pages):
                print(f"loading page {i + 1}")
                url = f"{base_url}&page={i + 1}"
                print(url)
                page = session.get(url, headers=headers)

                f = open(f"{search_term.replace(' ', '_')}-{i + 1}-out.html", 'w')
                f.write(page.text)

                page_brands = self.get_brands(page.text)
                print(f"found {len(page_brands)} brands on page")

        return brands

    def get_brands(self, html):
        regex = re.compile('"brandName":"([^"]+)"')
        matches = re.findall(regex, html)
        return matches
