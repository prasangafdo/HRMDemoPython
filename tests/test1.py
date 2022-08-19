import pytest
from page import loginpage


# Test should either start with test or end with test. Same applicable for python file

def test_user_can_login_with_valid_credentials():
    loginpage.load_login_page()
