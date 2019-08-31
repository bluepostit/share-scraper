from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Page:
    # seconds to wait for the page to load (eg. DOM changes with AJAX)
    PAGE_LOAD_MAX_WAIT = 15

    URL = None

    def __init__(self, browser):
        self.browser = browser

    def load(self, url=None):
        url = self.URL if url is None else url
        self.browser.get(url)
        return self

    def wait_for_css_selector(self, css_selector, max_wait=None):
        max_wait = self.PAGE_LOAD_MAX_WAIT if max_wait is None else max_wait
        try:
            WebDriverWait(self.browser, max_wait).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, css_selector)
                )
            )
            return True
        except TimeoutException:
            print("timed out")
            return None

    def open_new_tab(self):
        self.browser.find_element_by_tag_name('body').send_keys(
            Keys.CONTROL + 't')
        return self

    def close_tab(self):
        self.browser.find_element_by_tag_name('body').send_keys(
            Keys.CONTROL + 'w')
        return self
