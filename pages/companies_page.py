from pages.base_page import BasePage


class CompaniesPage(BasePage):

    PAGE_HEADING = "//h1[text()='Companies']"
    AUTO_REFRESH_CHECKBOX = "//label[.//span[normalize-space()='Auto-refresh']]//input[@type='checkbox']"
    REFRESH_BUTTON = "//button[normalize-space()='Refresh']"
    ALL_FILTER = "//button[starts-with(normalize-space(),'All')]"
    ADD_COMPANY_BUTTON = "//button[contains(normalize-space(),'Add Company')]"
    PLAN_DROPDOWN = "//select[@aria-label='Filter by plan']"
    TYPE_DROPDOWN = "//select[@aria-label='Filter by registration type']"
    FROM_DATE = "(//input[@type='date'])[1]"
    TO_DATE = "(//input[@type='date'])[2]"
    SEARCH_TEXTBOX = "//input[@placeholder='Search by Company Name, Email ID...']"
    COMPANIES_TABLE = "//table[contains(@class,'min-w-full')]"
    TABLE_HEADERS = "//table//thead//th"
    ADD_COMPANY_PAGE_HEADING = "//h1[normalize-space()='Add New Company']"
    COMPANY_INFORMATION_SECTION = "//h2[contains(normalize-space(),'Company Information')]"
    CREATE_COMPANY_BUTTON = "//button[normalize-space()='Create Company']"

    COMPANY_NAME_REQUIRED = "//p[normalize-space()='Company Name is required.']"

    # COUNTRY_REQUIRED = "//p[normalize-space()='Country is required.']"

    ADMIN_NAME_REQUIRED = "//p[normalize-space()='Admin Name is required.']"

    ADMIN_EMAIL_REQUIRED = "//p[normalize-space()='Admin Email ID is required.']"

    ADMIN_PASSWORD_REQUIRED = "//p[normalize-space()='Admin Password is required.']"

    VALIDATION_MESSAGES = "//p[contains(@class,'text-red-600')]"

    COMPANY_NAME_TEXTBOX = "//input[@placeholder='Enter Company Name']"

    COUNTRY_DROPDOWN = "//select[@name='country']"

    PURCHASE_COUNTRY_DROPDOWN = "//select[@name='purchaseCountry']"

    ADMIN_NAME_TEXTBOX = "//input[@placeholder='Enter Admin Name']"

    ADMIN_EMAIL_TEXTBOX = "//input[@placeholder='Enter Admin Email ID']"

    ADMIN_PASSWORD_TEXTBOX = "//input[@placeholder='Enter Admin Password']"

    PLAN_DROPDOWN_ADD_COMPANY = "//select[@name='planId']"

    VALIDITY_DROPDOWN = "//select[@name='validityMonths']"
    SEARCH_TEXTBOX = "//input[@placeholder='Search by Company Name, Email ID...']"
    DELETE_MENU = "//button[contains(@aria-label,'Actions')]"

    DELETE_OPTION = "//span[text()='Delete']"

    CONFIRM_DELETE = "//button[normalize-space()='Yes, Delete']"
    ACTION_BUTTON = (
    "//td[normalize-space()='{}']"
    "/following-sibling::td//button"
)
    DELETE_COMPANY_OPTION = (
    "//*[normalize-space()='Delete Company']"
)   
    CONFIRM_DELETE_BUTTON = (
    "//button[normalize-space()='Delete']"
)

    def __init__(self, page):
        super().__init__(page)

    def is_companies_page_displayed(self):

        return self.is_visible_with_wait(self.PAGE_HEADING)


    def get_page_heading(self):

        return self.get_text(self.PAGE_HEADING)

    def is_summary_card_displayed(self, card_name):
        locator = f"//p[normalize-space()='{card_name}']"
        return self.is_visible_with_wait(locator)

    def is_auto_refresh_checkbox_displayed(self):

        return self.is_visible_with_wait(self.AUTO_REFRESH_CHECKBOX)

    def is_auto_refresh_checked(self):
        return self.page.locator(self.AUTO_REFRESH_CHECKBOX).is_checked()
    
    #-------------referesh button----------------------

    def is_refresh_button_displayed(self):

        return self.is_visible_with_wait(self.REFRESH_BUTTON)

    def is_refresh_button_enabled(self):

        return self.page.locator(self.REFRESH_BUTTON).is_enabled()

    #---------------all filters--------------------

    def is_filter_displayed(self, filter_name):

        locator = f"//button[starts-with(normalize-space(),'{filter_name}')]"

        return self.is_visible_with_wait(locator)


    def is_filter_enabled(self, filter_name):

        locator = f"//button[starts-with(normalize-space(),'{filter_name}')]"

        return self.page.locator(locator).is_enabled()

    #--------------------------add company button-----------------

    def is_add_company_button_displayed(self):

        return self.is_visible_with_wait(self.ADD_COMPANY_BUTTON)


    def is_add_company_button_enabled(self):

        return self.page.locator(self.ADD_COMPANY_BUTTON).is_enabled()


    def click_add_company_button(self):

        print("Inside method - Before click:", self.get_current_url())

        self.page.screenshot(path="before_click.png")

        button = self.page.locator(self.ADD_COMPANY_BUTTON)

        print("Button count:", button.count())

        button.click()

        print("Inside method - After click:", self.get_current_url())


    def is_add_company_page_displayed(self):

        return self.is_visible_with_wait(self.ADD_COMPANY_PAGE_HEADING)

    # def click_create_company_button(self):

    #     self.click(self.CREATE_COMPANY_BUTTON)


    def get_required_field_validation_messages(self):

        validations = self.page.locator(self.VALIDATION_MESSAGES)

        validations.first.wait_for(state="visible")

        return [
            validations.nth(i).text_content().strip()
            for i in range(validations.count())
        ]

    def click_create_company_button(self):

        self.click(self.CREATE_COMPANY_BUTTON)

#-------------------create company-------------------------#

    def fill_company_name(self, company_name):
        self.fill(self.COMPANY_NAME_TEXTBOX, company_name)

    def fill_admin_name(self, admin_name):
        self.fill(self.ADMIN_NAME_TEXTBOX, admin_name)

    def fill_admin_email(self, email):
        self.fill(self.ADMIN_EMAIL_TEXTBOX, email)

    def fill_admin_password(self, password):
        self.fill(self.ADMIN_PASSWORD_TEXTBOX, password)

    def select_country(self, country):

        self.select_dropdown_by_text(
            self.COUNTRY_DROPDOWN,
            country
        )


    def select_purchase_country(self, country):

        self.select_dropdown_by_text(
            self.PURCHASE_COUNTRY_DROPDOWN,
            country
        )


    def select_plan(self, plan):

        self.select_dropdown_by_text(
            self.PLAN_DROPDOWN_ADD_COMPANY,
            plan
        )


    def select_validity(self, validity):

        self.select_dropdown_by_text(
            self.VALIDITY_DROPDOWN,
            validity
        )

    def search_company(self, company_name):

        self.fill(self.SEARCH_TEXTBOX, company_name)

        self.page.wait_for_timeout(1000)

    def is_company_present(self, company_name):

        locator = f"//td[normalize-space()='{company_name}']"

        return self.is_visible_with_wait(locator)

    def delete_company(self, company_name):

        self.page.locator(
            self.get_action_button_locator(company_name)
        ).click()

        self.click(self.DELETE_COMPANY_OPTION)

        self.click(self.CONFIRM_DELETE_BUTTON)

        self.page.wait_for_load_state("networkidle")


    def get_action_button_locator(self, company_name):

        return (
            f"//tr[td[normalize-space()='{company_name}']]"
            f"//button[@title='Actions']"
        )