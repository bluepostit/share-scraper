from math import ceil
import re
import requests
from .base import SimpleScraper


class LazadaSimpleScraper(SimpleScraper):
    RESULTS_PER_PAGE = 40

    SEARCH_URL = "https://www.lazada.vn/catalog/?q=##SEARCH_TERM##" \
        + "&_keyori=ss&from=input&spm=a2o4n.home.search.go.1905e18214cAJy"

    def get_page_source(self, url):
        params = {
            'api_key': self.scraper_api_key,
            'url': url
        }
        page = requests.get('http://api.scraperapi.com', params=params)
        return page.text

    def get_brand_shares(self, search_term, results_limit):
        base_url = self.SEARCH_URL.replace('##SEARCH_TERM##', search_term)
        amt_pages = ceil(results_limit / self.RESULTS_PER_PAGE)
        print(f"pages to load: {amt_pages}")

        brands = []

        # First page
        print(f"loading first page: {base_url}")

        page_text = self.get_page_source(base_url)
        brands += self.get_brands(page_text)
        print(f"found {len(brands)} brands on page")

        # Additional pages
        for i in range(1, amt_pages):
            url = f"{base_url}&page={i + 1}"
            print(f"loading page {i + 1}: {url}")
            page_text = self.get_page_source(url)

            page_brands = self.get_brands(page_text)
            print(f"found {len(page_brands)} brands on page")
            brands += page_brands

        return self._get_brands_as_shares(brands[:results_limit])

    def get_brands(self, html):
        regex = re.compile('"brandName":"([^"]+)"')
        matches = re.findall(regex, html)
        return matches
