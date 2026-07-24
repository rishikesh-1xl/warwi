import pytest

from utilities.config_reader import Config
from pages.login_page import LoginPage
from components.header import Header


@pytest.mark.tc_login_001
def test_verify_valid_login(login):

    login_page = LoginPage(login)

    assert login_page.is_dashboard_displayed()


@pytest.mark.tc_login_002
def test_verify_login_page_displayed(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_login_page_displayed()


@pytest.mark.tc_login_003
def test_verify_email_field_visible(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_email_visible()


@pytest.mark.tc_login_004
def test_verify_password_field_visible(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_password_visible()


@pytest.mark.tc_login_005
def test_verify_login_button_visible(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_login_button_visible()


@pytest.mark.tc_login_006
def test_verify_forgot_password_link_visible(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_forgot_password_visible()


@pytest.mark.tc_login_007
def test_verify_register_link_visible(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    assert login_page.is_register_visible()


@pytest.mark.tc_login_008
def test_verify_required_field_validation(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    login_page.click_login()

    assert login_page.get_email_required_message() == "Email ID is required."

    assert login_page.get_password_required_message() == "Password is required."


@pytest.mark.tc_login_009
def test_verify_password_required_validation(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    login_page.enter_email("admin@triton-testing.com")

    login_page.click_login()

    assert login_page.get_password_required_message() == "Password is required."


@pytest.mark.tc_login_010
def test_verify_password_policy_validation(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    login_page.enter_email("admin@triton-testing.com")

    login_page.enter_password("12345678")

    login_page.click_login()

    assert "Password must be" in login_page.get_password_policy_message()

@pytest.mark.tc_login_011
def test_verify_user_logout(login):

    header = Header(login)

    assert header.get_logged_in_username() != ""

    header.logout()

    login_page = LoginPage(login)

    assert login_page.is_login_page_displayed()

    