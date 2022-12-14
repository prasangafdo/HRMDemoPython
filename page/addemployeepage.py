import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver
lbl_add_user_topic = "//h6[normalize-space()='Add User']"
drp_dwn_user_role = "//div[normalize-space()='User Role']//ancestor::div[@class='oxd-input-group " \
                    "oxd-input-field-bottom-space']//div[@class='oxd-select-wrapper'] "
drp_dwn_admin = "//div[@role='listbox']//div[normalize-space()='Admin']"
drp_dwn_ess = "//div[@role='listbox']//div[normalize-space()='ESS']"
btn_save = "//button[normalize-space()='Save']"
txt_employee_name = "//input[@placeholder='Type for hints...']"
drp_dwn_employee_name = "//div[contains(@class,'oxd-autocomplete-dropdown')]"
drp_dwn_status = "//div[normalize-space()='Status']//ancestor::div[@class='oxd-input-group " \
                 "oxd-input-field-bottom-space']//div[@class='oxd-select-wrapper'] "
drp_dwn_status_enabled = "//div[@role='listbox']//div[normalize-space()='Enabled']"
txt_username = "//div[normalize-space()='Username']//input"
txt_password = "//div[normalize-space()='Password']//input"
txt_confirm_password = "//div[normalize-space()='Confirm Password']//input"
lbl_save_success_toast = "//div[@id='oxd-toaster_1']"


def add_a_new_admin_user():
    driver.find_element(By.XPATH, drp_dwn_user_role).click()
    driver.find_element(By.XPATH, drp_dwn_admin).click()
    driver.find_element(By.XPATH, txt_employee_name).send_keys("a")
    time.sleep(3)
    driver.find_element(By.XPATH, drp_dwn_employee_name).click()
    driver.find_element(By.XPATH, drp_dwn_status).click()
    driver.find_element(By.XPATH, drp_dwn_status_enabled).click()
    driver.find_element(By.XPATH, txt_username).send_keys("Automation_admin_user_002")
    driver.find_element(By.XPATH, txt_password).send_keys("Test@123")
    time.sleep(1)
    driver.find_element(By.XPATH, txt_confirm_password).send_keys("Test@123")
    time.sleep(2)
    driver.find_element(By.XPATH, btn_save).click()
    time.sleep(5)


def add_a_new_ess_user():
    driver.find_element(By.XPATH, drp_dwn_user_role).click()
    driver.find_element(By.XPATH, drp_dwn_ess).click()
    driver.find_element(By.XPATH, txt_employee_name).send_keys("a")
    time.sleep(3)
    driver.find_element(By.XPATH, drp_dwn_employee_name).click()
    driver.find_element(By.XPATH, drp_dwn_status).click()
    driver.find_element(By.XPATH, drp_dwn_status_enabled).click()
    driver.find_element(By.XPATH, txt_username).send_keys("Automation_ess_user_002")
    driver.find_element(By.XPATH, txt_password).send_keys("Test@123")
    time.sleep(1)
    driver.find_element(By.XPATH, txt_confirm_password).send_keys("Test@123")
    time.sleep(2)
    driver.find_element(By.XPATH, btn_save).click()
    time.sleep(5)


def is_add_user_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_add_user_topic)))
    return bool(driver.find_element(By.XPATH, lbl_add_user_topic).is_displayed())


def is_save_success_message_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_save_success_toast)))
    return bool(driver.find_element(By.XPATH, lbl_save_success_toast).is_displayed())

