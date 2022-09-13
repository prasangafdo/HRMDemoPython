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
    driver.find_element(By.XPATH, txt_username).send_keys(username)
    driver.find_element(By.XPATH, btn_search).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_rows)))
    return str(driver.find_element(By.XPATH, lbl_table_rows).text)
