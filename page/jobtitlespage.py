import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page import loginpage

driver = loginpage.driver

lbl_job_titles_topic = "//h6[text()='Job Titles']"
lbl_table_rows = "//div[@class='oxd-table-card']//div[contains(@class,'oxd-table-row')]"
btn_add_job_title = "//button[normalize-space()='Add']"
txt_job_title = "//div[normalize-space()='Job Title']//input"
lbl_save_success_toast = "//div[@id='oxd-toaster_1']"
btn_save = "//button[normalize-space()='Save']"


def is_job_titles_topic_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_job_titles_topic)))
    return driver.find_element(By.XPATH, lbl_job_titles_topic).is_displayed()


def are_table_data_not_empty():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_table_rows)))
    return bool(len(driver.find_element(By.XPATH, lbl_table_rows).text) > 0)


def click_on_add_job_title_button():
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, btn_add_job_title))).click()


def enter_job_title():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, txt_job_title))).send_keys("Test_job1")
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, btn_save))).click()


def is_save_success_message_displaying():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lbl_save_success_toast)))
    return bool(driver.find_element(By.XPATH, lbl_save_success_toast).is_displayed())


def click_on_edit_job_title_button():
    job_title = "Test_job1"
    btn_edit = "(//div[normalize-space()='" + job_title + "']//button)[2]"
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, btn_edit))).click()
