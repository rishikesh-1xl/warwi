from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADING = "//h1[contains(text(),'WhatsApp Status Automation Dashboard')]"

    AUTO_REFRESH_CHECKBOX = "//span[text()='Auto-refresh']/preceding-sibling::input"

    REFRESH_BUTTON = "//button[normalize-space()='Refresh']"

    LOGOUT_BUTTON = "//button[normalize-space()='Log Out']"

    TOTAL_EMPLOYEES_CARD = "//p[normalize-space()='Total Employees']"

    ACTIVE_EMPLOYEES_CARD = "//p[normalize-space()='Active Employees']"

    DELIVERIES_TODAY_CARD = "//p[normalize-space()='Deliveries Today']"

    FAILURES_TODAY_CARD = "//p[normalize-space()='Failures Today']"

    TOTAL_REVENUE_CARD = "//p[normalize-space()='Total Revenue']"

    MRR_CARD = "//p[normalize-space()='MRR']"

    ACTIVE_SUBSCRIPTIONS_CARD = "//p[normalize-space()='Active Subscriptions']"

    ON_TRIAL_CARD = "//p[normalize-space()='On Trial']"

    EXPIRING_TRIALS_CARD = "//p[normalize-space()='Expiring Trials']"

    PLAN_DISTRIBUTION_SECTION = "//h3[normalize-space()='Plan Distribution']"

    CONVERSION_RATE_SECTION = "//h3[normalize-space()='Conversion Rate']"

    UPDATED_TIMESTAMP = "//span[contains(normalize-space(),'Updated')]"

    def __init__(self, page):
        super().__init__(page)

    def is_dashboard_displayed(self):
        return self.is_visible_with_wait(self.DASHBOARD_HEADING)

    def get_current_url(self):
        return self.page.url

    def is_auto_refresh_checked(self):
        return self.page.locator(self.AUTO_REFRESH_CHECKBOX).is_checked()

    def is_refresh_button_visible(self):
        return self.is_visible_with_wait(self.REFRESH_BUTTON)

    def is_logout_button_visible(self):
        return self.is_visible_with_wait(self.LOGOUT_BUTTON)

    def get_dashboard_heading(self):

        return self.get_text(self.DASHBOARD_HEADING)

    def is_dashboard_heading_visible(self):

        return self.is_visible_with_wait(self.DASHBOARD_HEADING)

    def is_total_employees_card_visible(self):

        return self.is_visible_with_wait(self.TOTAL_EMPLOYEES_CARD)
    
    def is_active_employees_card_visible(self):

        return self.is_visible_with_wait(self.ACTIVE_EMPLOYEES_CARD)

    def is_deliveries_today_card_visible(self):

        return self.is_visible_with_wait(self.DELIVERIES_TODAY_CARD)

    def is_failures_today_card_visible(self):

        return self.is_visible_with_wait(self.FAILURES_TODAY_CARD)

    def is_total_revenue_card_visible(self):

        return self.is_visible_with_wait(self.TOTAL_REVENUE_CARD)

    def is_mrr_card_visible(self):

        return self.is_visible_with_wait(self.MRR_CARD)

    def is_active_subscriptions_card_visible(self):

        return self.is_visible_with_wait(self.ACTIVE_SUBSCRIPTIONS_CARD)

    def is_on_trial_card_visible(self):

        return self.is_visible_with_wait(self.ON_TRIAL_CARD)

    def is_expiring_trials_card_visible(self):

        return self.is_visible_with_wait(self.EXPIRING_TRIALS_CARD)

    def is_plan_distribution_section_visible(self):

        return self.is_visible_with_wait(self.PLAN_DISTRIBUTION_SECTION)

    def is_conversion_rate_section_visible(self):

        return self.is_visible_with_wait(self.CONVERSION_RATE_SECTION)

    def is_updated_timestamp_visible(self):

        return self.is_visible_with_wait(self.UPDATED_TIMESTAMP)