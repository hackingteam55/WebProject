from Browser import Browser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraping(Browser):

    ACCEPT_BUTTON = (By.XPATH, '//button[contains(text(), "Accept")]')
    FRAME = (By.ID, 'sp_message_iframe_1232217')

    def verify_element_is_displayed_by_selector(self, by, selector):
        elem = self.driver.find_element(by, selector)
        self.assertTrue(elem.is_displayed(), 'Elem not displayed')

    def wait_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def wait_for_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def open_page_and_do_stuff(self):
        self.driver.get('https://htmlcolorcodes.com')
        try:
            iframe = self.driver.find_element(*self.FRAME)
            self.driver.switch_to.frame(iframe)

            # Find the "Accept" button (adjust the selector based on the website)
            self.wait_and_click_elem_by_selector(*self.ACCEPT_BUTTON)

            print("Clicked on Accept button successfully.")

        except Exception as e:
            print("Accept button not found or could not be clicked:", e)


c = Scraping()
c.open_page_and_do_stuff()

