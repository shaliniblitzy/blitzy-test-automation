import pytest
from pages.login_page import LoginPage


def test_login_invalid_credentials(browser, config, credentials):
    login_page = LoginPage(browser)
    login_page.load(config["base_url"] + 'sign-in')
    
    login_page.enter_email(credentials["invalid"]["email"])
    login_page.enter_password(credentials["invalid"]["password"])
    login_page.click_login()
    
    assert "invalid" in login_page.get_error_message().lower()

def test_login_valid_credentials(browser, config, credentials):
    login_page = LoginPage(browser)
    login_page.load(config["base_url"] + 'sign-in')
    login_page.enter_email(credentials["valid"]["email"])
    login_page.enter_password(credentials["valid"]["password"])
    login_page.click_login()

    # Example validation — update based on actual page behavior after login
    assert "dashboard" in browser.current_url.lower()
