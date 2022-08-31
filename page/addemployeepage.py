from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver
lbl_add_user_topic = "//h6[normalize-space()='Add User']"


def add_a_new_admin_user():
    pass


def is_add_user_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_add_user_topic)))
    return bool(driver.find_element(By.XPATH, lbl_add_user_topic).is_displayed())
