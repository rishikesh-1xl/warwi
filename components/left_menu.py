from pages.base_page import BasePage


class LeftMenu(BasePage):

    # Main Menu
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

    # Organisation Sub Menu
    COMPANIES = "//span[text()='Companies']"
    PLANS = "//span[text()='Plans']"
    BILLING_DASHBOARD = "//span[text()='Billing Dashboard']"
    LEADS = "//span[normalize-space()='Leads']"
    LEAD_CONNECTORS = "//span[text()='Lead Connectors']"

    # Marketing Sub Menu

    COUPON_CODES = "//span[text()='Coupon Codes']"

    REFERRAL_PROGRAM = "//span[text()='Referral Program']"

    ANNOUNCEMENTS = "//span[text()='Announcements']"

    def __init__(self, page):
        super().__init__(page)

    # ---------------- Main Menu ---------------- #

    def click_dashboard(self):
        self.click(self.DASHBOARD)

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

    # ---------------- Organisation ---------------- #

    def open_organisation(self):

        # Expand only if collapsed
        if not self.page.locator(self.COMPANIES).is_visible():
            self.click(self.ORGANISATION)

    def close_organisation(self):

        if self.page.locator(self.COMPANIES).is_visible():
            self.click(self.ORGANISATION)

    # def click_companies(self):

    #     self.open_organisation()
    #     self.click(self.COMPANIES)

    def click_companies(self):

        print("Before:", self.page.url)

        self.click(self.ORGANISATION)

        self.page.wait_for_timeout(1000)

        print("Companies count:",
            self.page.locator(self.COMPANIES).count())

        self.page.locator(self.COMPANIES).first.click()

        self.page.wait_for_timeout(2000)

        print("After:", self.page.url)

    def click_plans(self):

        self.open_organisation()
        self.click(self.PLANS)

    def click_billing_dashboard(self):

        self.open_organisation()
        self.click(self.BILLING_DASHBOARD)

    def click_leads(self):

        self.open_organisation()
        self.click(self.LEADS)

    def click_lead_connectors(self):

        self.open_organisation()
        self.click(self.LEAD_CONNECTORS)

    # ---------------- Marketing ---------------- #

    def open_marketing(self):

        # Expand only if collapsed
        if not self.page.locator(self.COUPON_CODES).is_visible():
            self.click(self.MARKETING)

    def close_marketing(self):

        if self.page.locator(self.COUPON_CODES).is_visible():
            self.click(self.MARKETING)

    def click_coupon_codes(self):

        self.open_marketing()
        self.click(self.COUPON_CODES)


    def click_referral_program(self):

        self.open_marketing()
        self.click(self.REFERRAL_PROGRAM)


    def click_announcements(self):

        self.open_marketing()
        self.click(self.ANNOUNCEMENTS)

        #--------------------Leads---------------

    def click_leads(self):

        self.page.wait_for_load_state("networkidle")

        self.open_organisation()

        self.page.locator(self.LEADS).wait_for(state="visible")

        self.page.locator(self.LEADS).click()

        self.page.wait_for_url("**/leads")