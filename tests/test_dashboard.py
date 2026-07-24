import pytest


@pytest.mark.tc_dash_001
def test_verify_dashboard_page(dashboard_page):

    assert "dashboard" in dashboard_page.get_current_url().lower()

    assert dashboard_page.is_dashboard_displayed()


@pytest.mark.tc_dash_002
def test_verify_auto_refresh_checked_by_default(dashboard_page):

    assert dashboard_page.is_auto_refresh_checked()


@pytest.mark.tc_dash_003
def test_verify_refresh_button_visible(dashboard_page):

    assert dashboard_page.is_refresh_button_visible()


@pytest.mark.tc_dash_004
def test_verify_logout_button_visible(dashboard_page):

    assert dashboard_page.is_logout_button_visible()

@pytest.mark.tc_dash_005
def test_verify_dashboard_heading(dashboard_page):

    assert dashboard_page.is_dashboard_heading_visible()

    assert (
        dashboard_page.get_dashboard_heading()
        == "WhatsApp Status Automation Dashboard"
    )

@pytest.mark.tc_dash_006
def test_verify_total_employees_card(dashboard_page):

    assert dashboard_page.is_total_employees_card_visible()

@pytest.mark.tc_dash_007
def test_verify_active_employees_card(dashboard_page):

    assert dashboard_page.is_active_employees_card_visible()

@pytest.mark.tc_dash_008
def test_verify_deliveries_today_card(dashboard_page):

    assert dashboard_page.is_deliveries_today_card_visible()

@pytest.mark.tc_dash_009
def test_verify_failures_today_card(dashboard_page):

    assert dashboard_page.is_failures_today_card_visible()

@pytest.mark.tc_dash_010
def test_verify_total_revenue_card(dashboard_page):

    assert dashboard_page.is_total_revenue_card_visible()

@pytest.mark.tc_dash_011
def test_verify_mrr_card(dashboard_page):

    assert dashboard_page.is_mrr_card_visible()

@pytest.mark.tc_dash_012
def test_verify_active_subscriptions_card(dashboard_page):

    assert dashboard_page.is_active_subscriptions_card_visible()

@pytest.mark.tc_dash_013
def test_verify_on_trial_card(dashboard_page):

    assert dashboard_page.is_on_trial_card_visible()

@pytest.mark.tc_dash_014
def test_verify_expiring_trials_card(dashboard_page):

    assert dashboard_page.is_expiring_trials_card_visible()

@pytest.mark.tc_dash_015
def test_verify_plan_distribution_section(dashboard_page):

    assert dashboard_page.is_plan_distribution_section_visible()

@pytest.mark.tc_dash_016
def test_verify_conversion_rate_section(dashboard_page):

    assert dashboard_page.is_conversion_rate_section_visible()

@pytest.mark.tc_dash_017
def test_verify_updated_timestamp_display(dashboard_page):

    assert dashboard_page.is_updated_timestamp_visible()