from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

# class LandingPage(LoginPage):
img_banner = "//img[@alt='client brand banner']"
btn_admin = "//li[@class='oxd-main-menu-item-wrapper']/a[contains(@href,'viewAdminModule')]"


# arg = loginpage


def is_orange_hrm_logo_displaying():
    WebDriverWait(loginpage.driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, img_banner)))
    return loginpage.driver.find_element(By.XPATH, img_banner).is_displayed()


def navigate_to_admin_page():
    loginpage.driver.find_element(By.XPATH, btn_admin).click()


def quite_driver():
    loginpage.driver.quit()
