from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content().strip()

    def is_visible_with_wait(self, locator, timeout=10000):
        try:
            expect(self.page.locator(locator)).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def get_dropdown_options(self, locator, timeout=30000):

        select = self.page.locator(locator)
        options = select.locator("option")

        expect(options.nth(1)).to_be_attached(timeout=timeout)

        return [
            options.nth(i).text_content().strip()
            for i in range(options.count())
        ]

    def select_dropdown_by_text(self, locator, text):

        dropdown = self.page.locator(locator)

        try:
            dropdown.select_option(label=text)
        except:
            options = dropdown.locator("option")

            for i in range(options.count()):
                option = options.nth(i)

                option_text = option.text_content().strip()

                if text.lower() in option_text.lower():
                    value = option.get_attribute("value")
                    dropdown.select_option(value=value)
                    return

            raise Exception(f"'{text}' not found in dropdown")

    def get_validation_message(self, locator):

        return self.page.locator(locator).text_content().strip()

    def click_checkbox(self, locator):

        checkbox = self.page.locator(locator)

        checkbox.scroll_into_view_if_needed()

        checkbox.wait_for(state="visible")

        checkbox.check()

    def is_checkbox_checked(self, locator):

        return self.page.locator(locator).is_checked()

    def get_selected_dropdown_value(self, locator):

        return self.page.locator(locator).input_value()

    def get_selected_dropdown_text(self, locator):

        return (
            self.page.locator(locator)
            .locator("option:checked")
            .text_content()
            .strip()
        )

    def get_input_value(self, locator):

        return self.page.locator(locator).input_value()

    def get_attribute(self, locator, attribute):

        return self.page.locator(locator).get_attribute(attribute)

    def get_current_url(self):

        return self.page.url



    def get_table_headers(self, locator):

        headers = self.page.locator(locator)

        expect(headers.first).to_be_visible(timeout=10000)

        actual_headers = []

        for i in range(headers.count()):
            text = headers.nth(i).text_content().strip()

            if text:
                actual_headers.append(text)

        return actual_headers