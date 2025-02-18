import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class Browser(unittest.TestCase):
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.close()
