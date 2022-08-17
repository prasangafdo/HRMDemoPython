from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    driver = webdriver.Chrome(ChromeDriverManager().install())


def load_login_page(self):
    self.driver.set_page_load_timeout(10)
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
