from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    EMAIL = "//input[@placeholder='Enter Your Email ID']"
    PASSWORD = "//input[@placeholder='Enter Your Password']"
    LOGIN_BUTTON = "//button[normalize-space()='Log In']"

    DASHBOARD_HEADING = "//h1[contains(text(),'WhatsApp Status Automation Dashboard')]"

    FORGOT_PASSWORD = "text=Forgot Password?"
    REGISTER = "text=Register"

    EMAIL_REQUIRED = "text=Email ID is required."
    PASSWORD_REQUIRED = "text=Password is required."
    PASSWORD_POLICY = "text=Password must be"

    WELCOME_TEXT = "text=Welcome!"

    def __init__(self, page):
        super().__init__(page)

    # Navigation

    def navigate_to_login(self, base_url):

        self.page.goto(base_url)

    # Actions

    def login(self, email, password):

        self.enter_email(email)

        self.enter_password(password)

        self.click_login()

        expect(
            self.page.locator(self.DASHBOARD_HEADING)
        ).to_be_visible()

    def enter_email(self, email):

        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):

        self.enter_text(self.PASSWORD, password)

    def click_login(self):

        self.click(self.LOGIN_BUTTON)

    # Visibility

    def is_login_page_displayed(self):

        return (
            self.is_visible_with_wait(self.WELCOME_TEXT)
            and self.is_visible_with_wait(self.LOGIN_BUTTON)
        )

    def is_dashboard_displayed(self):

        return self.is_visible_with_wait(self.DASHBOARD_HEADING)

    def is_email_visible(self):

        return self.is_visible_with_wait(self.EMAIL)

    def is_password_visible(self):

        return self.is_visible_with_wait(self.PASSWORD)

    def is_login_button_visible(self):

        return self.is_visible_with_wait(self.LOGIN_BUTTON)

    def is_forgot_password_visible(self):

        return self.is_visible_with_wait(self.FORGOT_PASSWORD)

    def is_register_visible(self):

        return self.is_visible_with_wait(self.REGISTER)

    # Validation Messages

    def get_email_required_message(self):

        return self.get_text(self.EMAIL_REQUIRED)

    def get_password_required_message(self):

        return self.get_text(self.PASSWORD_REQUIRED)

    def get_password_policy_message(self):

        return self.get_text(self.PASSWORD_POLICY)