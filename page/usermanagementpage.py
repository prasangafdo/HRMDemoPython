from selenium.webdriver.common.by import By

from page import loginpage

lbl_admin_topic = "//span[@class='oxd-topbar-header-breadcrumb']"
lbl_table_body = "//div[@class='oxd-table-body']"


def is_admin_topic_displaying():
    return loginpage.driver.find_element(By.XPATH, lbl_admin_topic).is_displayed()


def are_column_headers_displaying():
    return len(loginpage.driver.find_element(By.XPATH, lbl_table_body).getText) > 0
    # pass  # Will work on this later after fixing the navigation
