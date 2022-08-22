import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from resources import constants


class LoginPage:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    lbl_username = "username"
    lbl_password = "password"
    btn_login = "//button[normalize-space()='Login']"

    def load_login_page(self):
        self.driver.set_page_load_timeout(10)
        self.driver.get(constants.baseURL)

    def login_with_valid_credentials(self):
        # time.sleep(5)
        self.driver.find_element(By.NAME, self.lbl_username).send_keys(constants.username)
        self.driver.find_element(By.NAME, self.lbl_password).send_keys(constants.password)
        self.driver.find_element(By.XPATH, self.btn_login).click()


