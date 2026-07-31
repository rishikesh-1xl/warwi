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

@pytest.mark.tc_leads_005
def test_verify_search_textbox_placeholder(leads_page):

    # Verify Leads page is displayed
    assert leads_page.is_leads_page_displayed()

    expected_placeholder = "Search by Name or Email ID..."

    actual_placeholder = leads_page.get_search_placeholder()

    assert actual_placeholder == expected_placeholder

@pytest.mark.tc_leads_006
def test_verify_subject_dropdown_displayed(leads_page):

    # Verify Leads page is displayed
    assert leads_page.is_leads_page_displayed()

    # Verify Subject dropdown is displayed
    assert leads_page.is_subject_dropdown_displayed()

@pytest.mark.tc_leads_007
def test_verify_subject_dropdown_values(leads_page):

    # Verify Leads page is displayed
    assert leads_page.is_leads_page_displayed()

    expected_values = [
        "All Subjects",
        "General Enquiry",
        "Request a Demo",
        "Pricing & Plans",
        "Technical Support",
        "Enterprise/Custom Plan",
        "Partnership"
    ]

    actual_values = leads_page.get_subject_dropdown_values()

    assert actual_values == expected_values

