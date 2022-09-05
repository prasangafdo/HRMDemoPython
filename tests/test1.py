import pytest
from page import loginpage
from page import landingpage , addemployeepage
from page import usermanagementpage


# Test should either start with test or end with test. Same applicable for python file

class TestRunner:

    def test_user_can_login_with_valid_credentials(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.quite_driver()

    def test_admin_can_view_all_users(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        assert bool(usermanagementpage.are_column_headers_displaying()) == True
        landingpage.quite_driver()

    # def test_admin_can_add_an_employee_without_login_details(self):
    #     loginpage.load_login_page()
    #     loginpage.login_with_valid_credentials()
    #     assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
    #     landingpage.navigate_to_admin_page()
    #     assert bool(usermanagementpage.is_admin_topic_displaying()) == True

    def test_admin_can_add_a_new_system_user(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        usermanagementpage.open_add_system_user_page()
        assert addemployeepage.is_add_user_topic_displaying() == True
        addemployeepage.add_a_new_admin_user()
        # completed the navigation to add user page
        landingpage.quite_driver()


