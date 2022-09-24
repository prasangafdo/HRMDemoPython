import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

lbl_admin_topic = "//span[@class='oxd-topbar-header-breadcrumb']"
lbl_table_body = "//div[@class='oxd-table-body']"
btn_add_system_user = "//button[normalize-space()='Add']"
txt_username = "//div[normalize-space()='Username']//input"
btn_search = "//button[normalize-space()='Search']"
lbl_table_rows = "//div[@class='oxd-table-card']//div[contains(@class,'oxd-table-row')]"
chk_user = "oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input"
btn_delete = "//button[normalize-space()='Delete Selected']"
brn_yes_delete = "//button[normalize-space()='Yes, Delete']"
lbl_save_success_toast = "//div[@id='oxd-toaster_1']"
driver = loginpage.driver


def is_admin_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_admin_topic)))
    return bool(driver.find_element(By.XPATH, lbl_admin_topic).is_displayed())


def are_column_headers_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_body)))
    return len(driver.find_element(By.XPATH, lbl_table_body).text) > 0


def open_add_system_user_page():
    driver.find_element(By.XPATH, btn_add_system_user).click()


def search_by_username(username):
    WebDriverWait(driver, 100).until(
        expected_conditions.element_to_be_clickable((By.XPATH, txt_username)))
    time.sleep(3)
    driver.find_element(By.XPATH, txt_username).send_keys(username)
    driver.find_element(By.XPATH, btn_search).click()
    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_rows)))
    time.sleep(3)
    return str(driver.find_element(By.XPATH, lbl_table_rows).text)


def tick_checkbox_and_delete():
    script = "document.getElementsByClassName('oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input')[0].click()"
    WebDriverWait(driver, 100).until(
        expected_conditions.element_to_be_clickable((By.XPATH, lbl_table_rows)))
    driver.execute_script(script)
    # driver.find_element(By.XPATH, chk_user).click()
    driver.find_element(By.XPATH, btn_delete).click()
    WebDriverWait (driver, 100).until(
        expected_conditions.element_to_be_clickable((By.XPATH, brn_yes_delete)))
    driver.find_element(By.XPATH, brn_yes_delete).click()
    time.sleep(5)


def is_delete_success_message_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_save_success_toast)))
    return bool(driver.find_element(By.XPATH, lbl_save_success_toast).is_displayed())
