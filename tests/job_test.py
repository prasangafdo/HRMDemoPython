import pytest
from page import jobtitlespage as job_title
from page import loginpage
from page import landingpage, addemployeepage, edituserpage
from page import usermanagementpage


class TestJobs:

    def test_admin_can_view_existing_job_titles(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        landingpage.navigate_to_job_titles()
        # assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        assert job_title.is_job_titles_topic_displaying() == True
        assert job_title.are_table_data_not_empty() == True
        landingpage.quite_driver()

    def test_admin_can_add_a_new_job_title(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        landingpage.navigate_to_job_titles()
        # assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        assert job_title.is_job_titles_topic_displaying() == True
        assert job_title.are_table_data_not_empty() == True
        job_title.click_on_add_job_title_button()
        job_title.enter_job_title()
        assert job_title.is_save_success_message_displaying() == True
        landingpage.quite_driver()

    def test_admin_can_edit_job_title(self):
        loginpage.load_login_page()
        loginpage.login_with_valid_credentials()
        assert bool(landingpage.is_orange_hrm_logo_displaying()) == True
        landingpage.navigate_to_admin_page()
        landingpage.navigate_to_job_titles()
        # assert bool(usermanagementpage.is_admin_topic_displaying()) == True
        assert job_title.is_job_titles_topic_displaying() == True
        assert job_title.are_table_data_not_empty() == True
        # job_title.click_on_add_job_title_button()
        # job_title.enter_job_title()
        # assert job_title.is_save_success_message_displaying() == True
        # landingpage.quite_driver()