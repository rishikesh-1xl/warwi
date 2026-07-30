import pytest
from utilities.config_reader import Config
from datetime import date, timedelta
from utilities.date_utils import DateUtils

from utilities.test_data_generator import TestDataGenerator




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

@pytest.mark.tc_companies_009
def test_verify_auto_refresh_checkbox(companies_page):

    assert companies_page.is_auto_refresh_checkbox_displayed()

    #---------------refresh u----------------

@pytest.mark.tc_companies_010
def test_verify_refresh_button(companies_page):

    assert companies_page.is_refresh_button_displayed()

    assert companies_page.is_refresh_button_enabled()

#---------------all filters---------------------------

@pytest.mark.tc_companies_012
def test_verify_all_filter(companies_page):

    assert companies_page.is_filter_displayed("All")
    assert companies_page.is_filter_enabled("All")

#--------------------------add company button-----------------

@pytest.mark.tc_companies_011
def test_verify_add_company_button(companies_page):

    assert companies_page.is_add_company_button_displayed()

    assert companies_page.is_add_company_button_enabled()

@pytest.mark.tc_companies_013
def test_verify_active_filter(companies_page):

    assert companies_page.is_filter_displayed("Active")
    assert companies_page.is_filter_enabled("Active")

@pytest.mark.tc_companies_014
def test_verify_inactive_filter(companies_page):

    assert companies_page.is_filter_displayed("Inactive")

    assert companies_page.is_filter_enabled("Inactive")


@pytest.mark.tc_companies_015
def test_verify_trial_filter(companies_page):

    assert companies_page.is_filter_displayed("Trial")

    assert companies_page.is_filter_enabled("Trial")


@pytest.mark.tc_companies_016
def test_verify_subscribed_filter(companies_page):

    assert companies_page.is_filter_displayed("Subscribed")

    assert companies_page.is_filter_enabled("Subscribed")


@pytest.mark.tc_companies_017
def test_verify_expired_filter(companies_page):

    assert companies_page.is_filter_displayed("Expired")

    assert companies_page.is_filter_enabled("Expired")


@pytest.mark.tc_companies_018
def test_verify_cancelled_filter(companies_page):

    assert companies_page.is_filter_displayed("Cancelled")

    assert companies_page.is_filter_enabled("Cancelled")


@pytest.mark.tc_companies_019
def test_verify_plan_dropdown(companies_page):

    assert companies_page.is_visible_with_wait(companies_page.PLAN_DROPDOWN)

    assert companies_page.page.locator(companies_page.PLAN_DROPDOWN).is_enabled()

# @pytest.mark.tc_companies_020
# def test_verify_plan_dropdown_values(companies_page):

#     expected_options = [
#         "All Plans",
#         "Diamond",
#         "Employee",
#         "Free Trial",
#         "Gold",
#         "Platinum",
#         "TATA",
#         "abc",
#         "No Plan"
#     ]

#     actual_options = companies_page.get_dropdown_options(
#         companies_page.PLAN_DROPDOWN
#     )

#     assert actual_options == expected_options


@pytest.mark.tc_companies_021
def test_verify_type_dropdown(companies_page):

    assert companies_page.is_visible_with_wait(
        companies_page.TYPE_DROPDOWN
    )

    assert companies_page.page.locator(
        companies_page.TYPE_DROPDOWN
    ).is_enabled()

@pytest.mark.tc_companies_022
def test_verify_type_dropdown_values(companies_page):

    expected_options = [
        "All Types",
        "Self",
        "Admin"
    ]

    actual_options = companies_page.get_dropdown_options(
        companies_page.TYPE_DROPDOWN
    )

    assert actual_options == expected_options


@pytest.mark.tc_companies_023
def test_verify_from_date_field(companies_page):

    assert companies_page.is_visible_with_wait(
        companies_page.FROM_DATE
    )

    assert companies_page.page.locator(
        companies_page.FROM_DATE
    ).is_enabled()

@pytest.mark.tc_companies_024
def test_verify_to_date_field(companies_page):

    assert companies_page.is_visible_with_wait(
        companies_page.TO_DATE
    )

    assert companies_page.page.locator(
        companies_page.TO_DATE
    ).is_enabled()

@pytest.mark.tc_companies_025
def test_verify_date_picker_opens(companies_page):

    companies_page.click(companies_page.FROM_DATE)

    assert companies_page.page.locator(
        companies_page.FROM_DATE
    ).evaluate("e => e === document.activeElement")


@pytest.mark.tc_companies_026
def test_verify_valid_date_range(companies_page):

    from_date = DateUtils.days_before(2)
    to_date = DateUtils.today()

    companies_page.fill(companies_page.FROM_DATE, from_date)
    companies_page.fill(companies_page.TO_DATE, to_date)

    assert companies_page.get_input_value(companies_page.FROM_DATE) == from_date
    assert companies_page.get_input_value(companies_page.TO_DATE) == to_date

@pytest.mark.tc_companies_027
def test_verify_invalid_date_range(companies_page):

    from_date = DateUtils.days_before(2)

    companies_page.fill(companies_page.FROM_DATE, from_date)

    assert companies_page.get_attribute(
    companies_page.TO_DATE,
    "min"
    ) == from_date


@pytest.mark.tc_companies_028
def test_verify_search_textbox(companies_page):

    assert companies_page.is_visible_with_wait(
        companies_page.SEARCH_TEXTBOX
    )

    assert companies_page.page.locator(
        companies_page.SEARCH_TEXTBOX
    ).is_enabled()

    assert companies_page.get_attribute(
        companies_page.SEARCH_TEXTBOX,
        "placeholder"
    ) == "Search by Company Name, Email ID..."

@pytest.mark.tc_companies_029
def test_verify_search_using_email(companies_page):

    # Generate unique test data
    data = TestDataGenerator.company()

    # ---------- Create Company ----------

    companies_page.click_add_company_button()

    assert companies_page.is_add_company_page_displayed()

    # Company Information
    companies_page.fill_company_name(data["company_name"])
    companies_page.select_country("India")
    companies_page.select_purchase_country("Not locked yet")

    # Admin Credentials
    companies_page.fill_admin_name(data["admin_name"])
    companies_page.fill_admin_email(data["admin_email"])
    companies_page.fill_admin_password(data["admin_password"])

    # Plan
    companies_page.select_plan("Free Trial (Free)")
    companies_page.select_validity("12 months")

    companies_page.click_create_company_button()

    assert companies_page.is_companies_page_displayed()

    # ---------- Search by Email ----------

    companies_page.search_company(data["admin_email"])

    

    assert companies_page.is_email_present(data["admin_email"])

    assert companies_page.get_company_count() == 1

    # ---------- Cleanup ----------

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_present(data["company_name"])


@pytest.mark.tc_companies_030
def test_verify_search_with_invalid_company_name(companies_page):

    # Generate unique test data
    data = TestDataGenerator.company()

    # ---------- Create Company ----------

    companies_page.click_add_company_button()

    assert companies_page.is_add_company_page_displayed()

    # Company Information
    companies_page.fill_company_name(data["company_name"])
    companies_page.select_country("India")
    companies_page.select_purchase_country("Not locked yet")

    # Admin Credentials
    companies_page.fill_admin_name(data["admin_name"])
    companies_page.fill_admin_email(data["admin_email"])
    companies_page.fill_admin_password(data["admin_password"])

    # Plan
    companies_page.select_plan("Free Trial (Free)")
    companies_page.select_validity("12 months")

    companies_page.click_create_company_button()

    assert companies_page.is_companies_page_displayed()

    # ---------- Search with Invalid Company Name ----------

    invalid_company = "InvalidCompany123456"

    companies_page.search_company(invalid_company)

    assert not companies_page.is_company_present(invalid_company)

    assert companies_page.get_company_count() == 0

    # ---------- Cleanup ----------

    companies_page.search_company(data["company_name"])

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_present(data["company_name"])


@pytest.mark.tc_companies_031
def test_verify_clear_search(companies_page):

    # Generate unique test data
    data = TestDataGenerator.company()

    # ---------- Create Company ----------

    companies_page.click_add_company_button()

    assert companies_page.is_add_company_page_displayed()

    # Company Information
    companies_page.fill_company_name(data["company_name"])
    companies_page.select_country("India")
    companies_page.select_purchase_country("Not locked yet")

    # Admin Credentials
    companies_page.fill_admin_name(data["admin_name"])
    companies_page.fill_admin_email(data["admin_email"])
    companies_page.fill_admin_password(data["admin_password"])

    # Plan
    companies_page.select_plan("Free Trial (Free)")
    companies_page.select_validity("12 months")

    companies_page.click_create_company_button()

    assert companies_page.is_companies_page_displayed()

    # ---------- Search Company ----------

    companies_page.search_company(data["company_name"])

    assert companies_page.is_company_present(data["company_name"])

    # ---------- Clear Search ----------

    companies_page.clear_search()

    assert companies_page.is_search_box_empty()

    # Verify company list is restored
    assert companies_page.get_company_count() > 1

    # ---------- Cleanup ----------

    companies_page.search_company(data["company_name"])

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_present(data["company_name"])


@pytest.mark.tc_companies_032
def test_verify_companies_table_displayed(companies_page):

    # Verify Companies page is displayed
    assert companies_page.is_companies_page_displayed()

    # Verify Companies table is displayed
    assert companies_page.is_companies_table_displayed()

@pytest.mark.tc_companies_033
def test_verify_companies_table_headers(companies_page):

    expected_headers = [
        "",                 # Checkbox column
        "SR. NO.",
        "Company Name",
        "Admin Details",
        "Type",
        "Plan",
        "Subscription",
        "Employees",
        "Expiry/Renewal",
        "Status",
        "Created Date",
        "Actions"
    ]

    actual_headers = companies_page.get_table_headers()

    assert actual_headers == expected_headers


@pytest.mark.tc_companies_034
def test_verify_add_company_page_opens(companies_page):

    companies_page.click_add_company_button()

    assert "/add-company" in companies_page.get_current_url()

    assert companies_page.is_add_company_page_displayed()

@pytest.mark.tc_companies_035
def test_verify_mandatory_fields(companies_page):

    companies_page.click_add_company_button()

    companies_page.click_create_company_button()

    expected_messages = [
        "Company Name is required.",
        "Admin Name is required.",
        "Admin Email ID is required.",
        "Admin Password is required."
    ]

    actual_messages = companies_page.get_required_field_validation_messages()

    assert actual_messages == expected_messages



@pytest.mark.tc_companies_036
def test_verify_successful_company_creation(companies_page):

    # Generate unique test data
    data = TestDataGenerator.company()

    # Open Add Company page
    companies_page.click_add_company_button()

    # Verify Add Company page is displayed
    assert companies_page.is_add_company_page_displayed()

    # ---------------- Company Information ---------------- #

    companies_page.fill_company_name(data["company_name"])
    companies_page.select_country("India")
    companies_page.select_purchase_country("Not locked yet")

    # ---------------- Admin Credentials ---------------- #

    companies_page.fill_admin_name(data["admin_name"])
    companies_page.fill_admin_email(data["admin_email"])
    companies_page.fill_admin_password(data["admin_password"])

    # ---------------- Plan & Subscription ---------------- #

    companies_page.select_plan("Free Trial (Free)")
    companies_page.select_validity("12 months")

    # ---------------- Create Company ---------------- #

    companies_page.click_create_company_button()

    # Verify redirected back to Companies page
    assert companies_page.is_companies_page_displayed()

    # ---------------- Verify Company Created ---------------- #

    companies_page.search_company(data["company_name"])

    assert companies_page.is_company_present(data["company_name"])

    # ---------------- Cleanup ---------------- #

    companies_page.delete_company(data["company_name"])

    # Verify Company Deleted
    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_present(data["company_name"])