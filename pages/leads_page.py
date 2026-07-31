from pages.base_page import BasePage


class LeadsPage(BasePage):

    # ---------- Locators ----------

    PAGE_HEADING = "//h1[normalize-space()='Lead Management']"
    ALL_CARD = "//button[starts-with(normalize-space(),'All')]"

    NEW_CARD = "//button[starts-with(normalize-space(),'New')]"

    CONTACTED_CARD = "//button[starts-with(normalize-space(),'Contacted')]"

    DEMO_SCHEDULED_CARD = "//button[contains(normalize-space(),'Demo Scheduled')]"

    CONVERTED_CARD = "//button[starts-with(normalize-space(),'Converted')]"

    LOST_CARD = "//button[starts-with(normalize-space(),'Lost')]"
    SEARCH_TEXTBOX = "//input[@placeholder='Search by Name or Email ID...']"



    def __init__(self, page):
        super().__init__(page)

    # ---------- Verification Methods ----------

    def is_leads_page_displayed(self):
        return self.is_visible_with_wait(self.PAGE_HEADING)

    def get_page_heading(self):
        return self.get_text(self.PAGE_HEADING)

    def is_summary_card_displayed(self, card_name):

        locator = (
            f"//button[starts-with(normalize-space(),'{card_name}')]"
        )

        return self.is_visible_with_wait(locator)

    def is_search_textbox_displayed(self):
        return self.is_visible_with_wait(self.SEARCH_TEXTBOX)