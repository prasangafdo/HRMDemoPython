import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver

lbl_job_titles_topic = "//h6[text()='Job Titles']"
lbl_table_rows = "//div[@class='oxd-table-card']//div[contains(@class,'oxd-table-row')]"


def is_job_titles_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_job_titles_topic)))
    return driver.find_element(By.XPATH, lbl_job_titles_topic).is_displayed()


def are_table_data_not_empty():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_rows)))
    return bool(len(driver.find_element(By.XPATH, lbl_table_rows).text)>0)
