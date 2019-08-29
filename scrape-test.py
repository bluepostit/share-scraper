import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL_HOME = 'https://www.lazada.vn/'
URL_SEARCH = 'https://www.lazada.vn/catalog/?'
URL_SEARCH_SPECIFIC = 'https://www.lazada.vn/catalog/?q=#KEYWORD#&_keyori=ss&from=input&spm=a2o4n.searchlist.search.go.12e867042bEq61'


def get_search_data(page):
    soup = bs(page, 'html')
    # 'div.lzd-nav-search form'


def two():
    with requests.session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        home_page = session.get(URL_HOME, headers=headers)
        f = open('out.html', 'w')
        f.write(home_page.text)

        # search_data = get_search_data(home_page)
        # results_page = session.get(URL_SEARCH, data=search_data)


def one():
    with requests.session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        url = URL_SEARCH_SPECIFIC.replace('#KEYWORD#', 'drone')
        page = session.get(url, headers=headers)
        f = open('out.html', 'w')
        f.write(page.text)


def three():
    browser = webdriver.Firefox()
    browser.get(URL_HOME)
    q_element = browser.find_element_by_id('q')
    q_element.send_keys('drone')
    search_form = browser.find_element_by_css_selector('.lzd-nav-search > form')
    results_page = search_form.submit()
    html = browser.page_source
    # soup = bs(html)

    f = open('out.html', 'w')
    f.write(html)

    browser.quit()




three()
