import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver

btn_edit_user = "//i[@class='oxd-icon bi-pencil-fill']/parent::button"
lbl_edit_user_topic = "//h6[normalize-space()='Edit User']"
txt_user_name = "//div[normalize-space()='Username']//parent::div[contains(@class,'oxd-input-field-bottom-space')]//input"
btn_save = "//button[normalize-space()='Save']"


def is_edit_icon_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, btn_edit_user)))
    return driver.find_element(By.XPATH, btn_edit_user).is_displayed()


def is_edit_user_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_edit_user_topic)))
    return bool(driver.find_element(By.XPATH, lbl_edit_user_topic).is_displayed())


def navigate_to_edit_page():
    driver.find_element(By.XPATH, btn_edit_user).click()


def edit_username_and_save():
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, txt_user_name)))
    driver.find_element(By.XPATH, txt_user_name).send_keys('Automation_update_01')
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, btn_save)))
    driver.find_element(By.XPATH, btn_save).click()
