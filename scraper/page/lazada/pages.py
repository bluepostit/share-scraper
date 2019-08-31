from ..base import Page as BasePage

class HomePage(BasePage):
    URL = 'https://www.lazada.vn/'

    SEARCH_INPUT_ID = 'q'

    SEARCH_FORM_CSS = '.lzd-nav-search > form'

    def search(self, term):
        self.wait_for_css_selector(self.SEARCH_FORM_CSS)
        search_input = self.browser.find_element_by_id(self.SEARCH_INPUT_ID)
        search_input.send_keys(term)
        search_form = self.browser.find_element_by_css_selector(
            self.SEARCH_FORM_CSS)
        search_form.submit()


class SearchPage(BasePage):
    PAGE_LOADED_CSS_MARKER = 'div[data-qa-locator="product-item"]'

    SEARCH_RESULT_CSS_SELECTOR = 'div[data-qa-locator="product-item"]'

    def get_results(self):
        product_urls = []
        loaded = self.wait_for_css_selector(self.PAGE_LOADED_CSS_MARKER)

        if loaded:
            products = self.browser.find_elements_by_css_selector(
                self.SEARCH_RESULT_CSS_SELECTOR)
            print(f"There are {len(products)} products on the page")

            # scroll to end to force-load all images, then scroll back up
            # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # time.sleep(1)
            # browser.execute_script('window.scrollTo(0, 0)')


            links = [product.find_element_by_tag_name('a') for product in products]
            product_urls = [link.get_attribute('href') for link in links]
        return product_urls


class ProductPage(BasePage):
    BRAND_LINK_CSS = '.pdp-product-brand__brand-link'

    def get_brand(self):
        brand = None
        loaded = self.wait_for_css_selector(self.BRAND_LINK_CSS)
        if loaded:
            brand_link = self.browser.find_element_by_css_selector(
                self.BRAND_LINK_CSS)
            brand = brand_link.get_attribute('text')
        return brand
