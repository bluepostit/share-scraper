from math import ceil
from ..browser import ScraperBrowser
from ..page.lazada.pages import HomePage, ProductPage, SearchPage
from .base import Scraper

class LazadaScraper(Scraper):
    RESULTS_PER_PAGE = 40

    def get_brand_share(self, search_term, results_limit):
        results = []
        amt_pages = ceil(results_limit / self.RESULTS_PER_PAGE)

        home_page = HomePage(self.browser)
        home_page.load().search(search_term)
        print("searched!")

        # First page
        search_page = SearchPage(self.browser)
        self._wait_for_search_results(self.browser)
        base_url = self.browser.current_url
        brands = self.get_brands(search_page)

        # Additional pages
        for i in range(1, amt_pages):
            url = f"{base_url}&page={i + 1}"
            self.browser.get(url)
            search_page = SearchPage(self.browser)
            self._wait_for_search_results(self.browser)
            brands += self.get_brands(search_page)


        # page_results = search_page.get_results()
        # results += page_results


        # base_url = self.browser.current_url
        # search_urls = [base_url]
        # for i in range(1, amt_pages):
        #     search_urls.append(f"{base_url}&page={i + 1}")

        # print("search page urls:")
        # [print(url) for url in search_urls]

        # eager_browser = self.browser
        # for url in search_urls:
        #     self.browser.get(url)
        #     search_page = SearchPage(self.browser)
        #     page_results = search_page.get_results()
        #     results += page_results

        # print("search result urls:")
        # print(results)

        # for result in results[0:4]:
        #     product_page = ProductPage(self.browser)
        #     product_page.open_new_tab().load(result)
        #     brand = product_page.get_brand()
        #     print(f"Brand: {brand}")
        #     product_page.close_tab()

        return brands

    def get_brands(self, search_page):
        brands = []
        page_results = search_page.get_results()
        for result in page_results:
            product_page = ProductPage(self.browser)
            product_page.open_new_tab().load(result)
            brand = product_page.get_brand()
            print(f"Brand: {brand}")
            product_page.close_tab()
            brands.append(brand)
        return brands


    def _wait_for_search_results(self, browser):
        search_page = SearchPage(browser)
        search_page.wait_for_results_load()

