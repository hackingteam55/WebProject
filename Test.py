from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# aici se seteaza driver-ul de chrome (il descarca)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# seteaza timpul de asteptare pentru toate elementele care vor fi cautate mai tarziu
driver.implicitly_wait(10)
# atata asteapta sa se incarce pagina pana sa dea eroare, daca pagina nu se incarca in 10 sec da eroare
driver.set_page_load_timeout(10)
# face pagina full page
driver.maximize_window()
# sterge cookie-urile pentru sesiune
driver.delete_all_cookies()


# setam o constanta (e tot o variabila scrisa cu majuscule) pentru butonul de accept pe care o folosim mai jos
ACCEPT_BUTTON = (By.XPATH, '//button[contains(text(), "Accept")]')
# setam constanta pentru frame-ul de privacy
FRAME = (By.ID, 'sp_message_iframe_1232217')

# o functie care asteapta dupa un element si da click pe el
def wait_and_click_elem_by_selector(by, selector):
    # aici asteapta 5 secunde dupa un element sa fie clickable
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, selector)))
    # aici da click
    driver.find_element(by, selector).click()


def open_page_and_do_stuff():
    # get-ul deschide efectiv pagina web
    driver.get('https://htmlcolorcodes.com')
    try:
        # aici cautam frameul "FRAME" si daca il gasim il salvam in "iframe", daca nu il gaseste o sa crape
        iframe = driver.find_element(*FRAME)
        # aici facem switch la "iframe"
        driver.switch_to.frame(iframe)

        # aici asteptam si daca gasim elementul dam click pe el
        wait_and_click_elem_by_selector(*ACCEPT_BUTTON)

        print("Clicked on Accept button successfully.")

    except Exception as e:
        print("Accept button not found or could not be clicked:", e)


open_page_and_do_stuff()
