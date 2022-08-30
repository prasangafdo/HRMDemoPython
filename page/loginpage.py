import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from resources import constants

driver = webdriver.Chrome(ChromeDriverManager().install())

lbl_username = "username"
lbl_password = "password"
btn_login = "//button[normalize-space()='Login']"


def load_login_page():
    driver.set_page_load_timeout(10)
    driver.get(constants.baseURL)
    driver.maximize_window()


def login_with_valid_credentials():
    # time.sleep(5)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.NAME, lbl_username)))
    driver.find_element(By.NAME, lbl_username).send_keys(constants.username)
    driver.find_element(By.NAME, lbl_password).send_keys(constants.password)
    driver.find_element(By.XPATH, btn_login).click()
