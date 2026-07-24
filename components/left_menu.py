from pages.base_page import BasePage


class LeftMenu(BasePage):

    DASHBOARD = "//span[text()='Dashboard']"

    ORGANISATION = "//span[text()='Organisation']"

    MARKETING = "//span[text()='Marketing']"

    PLATFORM_USERS = "//span[text()='Platform Users']"

    SCHEDULE_MANAGEMENT = "//span[text()='Schedule Management']"

    STATUS_HISTORY = "//span[text()='Status History']"

    EMAIL_LOGS = "//span[text()='Email Logs']"

    NOTIFICATIONS = "//span[text()='Notifications']"

    HELP_SUPPORT = "//span[text()='Help & Support']"

    ADMIN_TOOLS = "//span[text()='Admin Tools']"

    USER_MANUAL = "//span[text()='User Manual']"

    def __init__(self, page):
        super().__init__(page)

    def click_dashboard(self):
        self.click(self.DASHBOARD)

    def click_organisation(self):
        self.click(self.ORGANISATION)

    def click_marketing(self):
        self.click(self.MARKETING)

    def click_platform_users(self):
        self.click(self.PLATFORM_USERS)

    def click_schedule_management(self):
        self.click(self.SCHEDULE_MANAGEMENT)

    def click_status_history(self):
        self.click(self.STATUS_HISTORY)

    def click_email_logs(self):
        self.click(self.EMAIL_LOGS)

    def click_notifications(self):
        self.click(self.NOTIFICATIONS)

    def click_help_support(self):
        self.click(self.HELP_SUPPORT)

    def click_admin_tools(self):
        self.click(self.ADMIN_TOOLS)

    def click_user_manual(self):
        self.click(self.USER_MANUAL)