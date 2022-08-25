from selenium.webdriver.common.by import By

from page import loginpage

# class LandingPage(LoginPage):
img_banner = "//img[@alt='client brand banner']"

arg = loginpage


def is_orange_hrm_logo_displaying():
    return loginpage.driver.find_element(By.XPATH, img_banner).is_displayed()


def quite_driver():
    loginpage.driver.quit()
