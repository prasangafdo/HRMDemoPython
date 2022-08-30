from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

lbl_admin_topic = "//span[@class='oxd-topbar-header-breadcrumb']"
lbl_table_body = "//div[@class='oxd-table-body']"

driver = loginpage.driver


def is_admin_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_admin_topic)))
    return bool(driver.find_element(By.XPATH, lbl_admin_topic).is_displayed())


def are_column_headers_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_body)))
    return len(driver.find_element(By.XPATH, lbl_table_body).text) > 0
    # pass  # Will work on this later after fixing the navigation
