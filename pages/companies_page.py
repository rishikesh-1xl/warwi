from pages.base_page import BasePage


class CompaniesPage(BasePage):

    PAGE_HEADING = "//h1[text()='Companies']"


    def __init__(self, page):
        super().__init__(page)

    def is_companies_page_displayed(self):

        return self.is_visible_with_wait(self.PAGE_HEADING)


    def get_page_heading(self):

        return self.get_text(self.PAGE_HEADING)

    def is_summary_card_displayed(self, card_name):
        locator = f"//p[normalize-space()='{card_name}']"
        return self.is_visible_with_wait(locator)