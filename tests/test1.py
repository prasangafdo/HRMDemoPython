import pytest
import softest
from page.loginpage import LoginPage


# Test should either start with test or end with test. Same applicable for python file

class TestRunner:

    def test_user_can_login_with_valid_credentials(self):
        login = LoginPage()
        login.load_login_page()
        login.login_with_valid_credentials()
