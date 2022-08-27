from selenium.webdriver.common.by import By

from page import loginpage

lbl_admin_topic = "//span[@class='oxd-topbar-header-breadcrumb']"


def is_admin_topic_displaying():
    loginpage.driver.find_element(By.XPATH, lbl_admin_topic).is_displayed()


def are_column_headers_displaying():
    pass  # Will work on this later after fixing the navigation
