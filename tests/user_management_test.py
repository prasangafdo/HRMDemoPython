import pytest
from page import loginpage
from page import landingpage, addemployeepage, edituserpage
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
        assert addemployeepage.is_save_success_message_displaying() == True
        usermanagementpage.open_add_system_user_page()
        assert addemployeepage.is_add_user_topic_displaying() == True
        addemployeepage.add_a_new_admin_user()
        assert addemployeepage.is_save_success_message_displaying() == True
        landingpage.quite_driver()

    def test_admin_can_search_a_system_user_by_username(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        username = "Fiona.Grace"
        assert username in usermanagementpage.search_by_username(username)
        landingpage.quite_driver()

    def test_admin_can_delete_a_system_user(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        username = "Fiona.Grace"
        assert username in usermanagementpage.search_by_username(username)
        usermanagementpage.tick_checkbox_and_delete()
        assert addemployeepage.is_save_success_message_displaying() == True
        landingpage.quite_driver()

    def test_admin_can_edit_a_system_user(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        username = "Fiona.Grace"
        assert username in usermanagementpage.search_by_username(username)
        assert edituserpage.is_edit_icon_displaying() == True
        edituserpage.navigate_to_edit_page()
        assert edituserpage.is_edit_user_topic_displaying() == True
        edituserpage.edit_username_and_save()
        landingpage.quite_driver()

