from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver
lbl_add_user_topic = "//h6[normalize-space()='Add User']"
drp_dwn_user_role = "//div[normalize-space()='User Role']//ancestor::div[@class='oxd-input-group " \
                "oxd-input-field-bottom-space']//div[@class='oxd-select-wrapper'] "
drp_dwn_admin = "//div[@role='listbox']//div[normalize-space()='Admin']"

btn_save = "//button[normalize-space()='Save']"


def add_a_new_admin_user():
    driver.find_element(By.XPATH, drp_dwn_user_role).click()
    driver.find_element(By.XPATH, drp_dwn_admin).click()
    driver.find_element(By.XPATH, btn_save).click()


def is_add_user_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_add_user_topic)))
    return bool(driver.find_element(By.XPATH, lbl_add_user_topic).is_displayed())
# //div[@class='oxd-select-wrapper']