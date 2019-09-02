from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class ScraperBrowser(webdriver.Firefox):
    '''A wrapper to Selenium webdriver's Firefox browser class.
    This defaults to using the 'eager' page loading strategry,
    and to running headless.'''
    def __init__(self, headless=True, eager=True):
        capabilities = DesiredCapabilities().FIREFOX
        options = FirefoxOptions()
        if eager:
            capabilities['pageLoadStrategy'] = 'eager'
        if headless:
            options.headless = True
        super().__init__(capabilities=capabilities, options=options)

    def get(self, url):
        print(f"get({url})")
        return super().get(url)
