from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver

btn_edit_user = "//i[@class='oxd-icon bi-pencil-fill']/parent::button"


def is_edit_icon_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, btn_edit_user)))
    return driver.find_element(By.XPATH, btn_edit_user).is_displayed()
