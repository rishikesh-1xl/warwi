import pytest
from utilities.config_reader import Config


@pytest.mark.tc_companies_001
def test_verify_navigation_to_companies_page(companies_page):

    assert "companies" in companies_page.get_current_url().lower()

    assert companies_page.is_companies_page_displayed()


@pytest.mark.tc_companies_002
def test_verify_companies_page_url(companies_page):

    expected_url = f"{Config.BASE_URL}/companies"

    assert companies_page.get_current_url() == expected_url

@pytest.mark.tc_companies_003
def test_verify_companies_page_heading(companies_page):

    assert companies_page.get_page_heading() == "Companies"

@pytest.mark.tc_companies_004
def test_verify_total_companies_card(companies_page):

    assert companies_page.is_summary_card_displayed("Total Companies")

@pytest.mark.tc_companies_005
def test_verify_active_companies_card(companies_page):

    assert companies_page.is_summary_card_displayed("Active")

@pytest.mark.tc_companies_006
def test_verify_on_trial_card(companies_page):

    assert companies_page.is_summary_card_displayed("On Trial")

@pytest.mark.tc_companies_007
def test_verify_active_subscription_card(companies_page):

    assert companies_page.is_summary_card_displayed("Active Subscriptions")

@pytest.mark.tc_companies_008
def test_verify_expired_card(companies_page):

    assert companies_page.is_summary_card_displayed("Expired")