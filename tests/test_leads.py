import pytest


@pytest.mark.tc_leads_001
def test_verify_leads_page_displayed(leads_page):

    assert leads_page.is_leads_page_displayed()


@pytest.mark.tc_leads_002
def test_verify_leads_page_heading(leads_page):

    expected_heading = "Lead Management"

    actual_heading = leads_page.get_page_heading()

    assert actual_heading == expected_heading

@pytest.mark.tc_leads_003
def test_verify_summary_cards_displayed(leads_page):

    summary_cards = [
        "All",
        "New",
        "Contacted",
        "Demo Scheduled",
        "Converted",
        "Lost"
    ]

    for card in summary_cards:

        assert leads_page.is_summary_card_displayed(card), \
            f"{card} summary card is not displayed."

@pytest.mark.tc_leads_004
def test_verify_search_textbox_displayed(leads_page):

    # Verify Leads page is displayed
    assert leads_page.is_leads_page_displayed()

    # Verify Search textbox is displayed
    assert leads_page.is_search_textbox_displayed()

