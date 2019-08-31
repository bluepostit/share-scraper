from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class EagerBrowser(webdriver.Firefox):
    '''A wrapper to Selenium webdriver's Firefox browser class.
    This defaults to using the 'eager' page loading strategry,
    and to running headless.'''
    def __init__(self):
        capabilities = DesiredCapabilities().FIREFOX
        capabilities['pageLoadStrategy'] = 'eager'
        options = FirefoxOptions()
        options.headless = True
        super().__init__(capabilities=capabilities, options=options)
