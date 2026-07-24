from pages.base_page import BasePage


class Header(BasePage):

    PROFILE_NAME = "//span[contains(@class,'text-sm') and contains(@class,'font-medium')]"

    LOGOUT_BUTTON = "//button[normalize-space()='Log Out']"

    LOGOUT_SUCCESS_MESSAGE = "text=Logged out successfully."

    def __init__(self, page):
        super().__init__(page)

    def click_logout(self):

        self.click(self.LOGOUT_BUTTON)

    def logout(self):

        self.click_logout()

    def is_profile_displayed(self):

        return self.is_visible_with_wait(self.PROFILE_NAME)

    def is_logout_button_visible(self):

        return self.is_visible_with_wait(self.LOGOUT_BUTTON)

    def is_logout_success_message_displayed(self):

        return self.is_visible_with_wait(self.LOGOUT_SUCCESS_MESSAGE)

    def get_logged_in_username(self):

        return self.get_text(self.PROFILE_NAME)