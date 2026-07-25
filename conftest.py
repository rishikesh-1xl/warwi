import os
import pytest

from dotenv import load_dotenv
from playwright.sync_api import Playwright

from utilities.config_reader import Config

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from components.left_menu import LeftMenu
from pages.companies_page import CompaniesPage
from pages.plans_page import PlansPage
from pages.billing_dashboard_page import BillingDashboardPage
from pages.leads_page import LeadsPage
from pages.lead_connectors_page import LeadConnectorsPage

from pages.coupon_codes_page import CouponCodesPage
from pages.referral_program_page import ReferralProgramPage
from pages.announcements_page import AnnouncementsPage

...

@pytest.fixture(scope="function")
def companies_page(login):

    menu = LeftMenu(login)

    menu.click_companies()

    return CompaniesPage(login)

load_dotenv()


@pytest.fixture(scope="function")
def page(playwright: Playwright):

    browser = playwright.chromium.launch(
        headless=Config.HEADLESS
    )

    context = browser.new_context(
        viewport={
            "width": Config.VIEWPORT_WIDTH,
            "height": Config.VIEWPORT_HEIGHT
        },
        record_video_dir="videos/"
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    page.set_default_timeout(Config.TIMEOUT)

    yield page

    os.makedirs("traces", exist_ok=True)

    context.tracing.stop(
        path="traces/trace.zip"
    )

    context.close()

    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            page.screenshot(
                path=f"screenshots/{item.name}.png",
                full_page=True
            )


@pytest.fixture(scope="function")
def login(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(
        Config.BASE_URL
    )

    login_page.login(
        os.getenv("WARWI_USERNAME"),
        os.getenv("WARWI_PASSWORD")
    )

    yield page


@pytest.fixture(scope="function")
def dashboard_page(login):

    return DashboardPage(login)

@pytest.fixture(scope="function")
def dashboard_page(login):
    return DashboardPage(login)

#---------------Organisation Sub menus-------------------#

@pytest.fixture(scope="function")
def companies_page(login):

    menu = LeftMenu(login)

    menu.click_companies()

    return CompaniesPage(login)

@pytest.fixture(scope="function")
def plans_page(login):

    menu = LeftMenu(login)

    menu.click_plans()

    return PlansPage(login)


@pytest.fixture(scope="function")
def billing_dashboard_page(login):

    menu = LeftMenu(login)

    menu.click_billing_dashboard()

    return BillingDashboardPage(login)


@pytest.fixture(scope="function")
def leads_page(login):

    menu = LeftMenu(login)

    menu.click_leads()

    return LeadsPage(login)


@pytest.fixture(scope="function")
def lead_connectors_page(login):

    menu = LeftMenu(login)

    menu.click_lead_connectors()

    return LeadConnectorsPage(login)

#---------------------Marketing sub menus----------------

@pytest.fixture(scope="function")
def coupon_codes_page(login):

    menu = LeftMenu(login)

    menu.click_coupon_codes()

    return CouponCodesPage(login)


@pytest.fixture(scope="function")
def referral_program_page(login):

    menu = LeftMenu(login)

    menu.click_referral_program()

    return ReferralProgramPage(login)


@pytest.fixture(scope="function")
def announcements_page(login):

    menu = LeftMenu(login)

    menu.click_announcements()

    return AnnouncementsPage(login)