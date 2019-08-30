import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



URL_HOME = 'https://www.lazada.vn/'
SEARCH_TERMS = ['ipod', 'handbag', 'Webcam logitech', 'Mp3 player']
# URL_SEARCH = 'https://www.lazada.vn/catalog/?'
# URL_SEARCH_SPECIFIC = 'https://www.lazada.vn/catalog/?q=#KEYWORD#&_keyori=ss&from=input&spm=a2o4n.searchlist.search.go.12e867042bEq61'


def three():
    search_term = random.choice(SEARCH_TERMS)
    browser = webdriver.Firefox()
    browser.get(URL_HOME)
    q_element = browser.find_element_by_id('q')
    q_element.send_keys(search_term)
    search_form = browser.find_element_by_css_selector('.lzd-nav-search > form')
    search_form.submit()

    # wait for page to be loaded by ajax
    delay = 10 # seconds
    try:
        products = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-qa-locator="product-item"]')
            )
        )
        products = browser.find_elements_by_css_selector(
            'div[data-qa-locator="product-item"]')
        print(f"There are {len(products)} products on the page")

        # scroll to end to force-load all images, then scroll back up
        # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(1)
        # browser.execute_script('window.scrollTo(0, 0)')


        i = 1
        links = [product.find_element_by_tag_name('a') for product in products]
        product_urls = [link.get_attribute('href') for link in links]
        for url in [product_urls[0]]:
            print(f"{i}\tproduct URL: {url}")
            # open a new tab
            browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            browser.get(url)
            brand_link = browser.find_element_by_class_name(
                'pdp-product-brand__brand-link')
            brand = brand_link.get_attribute('text')
            print(f"Brand: {brand}")

            # close the tab
            browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
            i += 1
    except TimeoutException:
        print("That took too long!")

    # browser.quit()


three()
