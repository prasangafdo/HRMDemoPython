from operator import truth

import pytest
from page import loginpage
from page import landingpage


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
        
        landingpage.quite_driver()
