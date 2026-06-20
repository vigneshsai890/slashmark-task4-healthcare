from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    _dropdown = (By.ID, "dropdown")

    def open(self):
        self.driver.get(self.URL)
        return self

    def select_by_text(self, text):
        select = Select(self.find(*self._dropdown))
        select.select_by_visible_text(text)

    def select_by_value(self, value):
        select = Select(self.find(*self._dropdown))
        select.select_by_value(value)

    def get_selected_text(self):
        select = Select(self.find(*self._dropdown))
        return select.first_selected_option.text

    def get_all_options(self):
        select = Select(self.find(*self._dropdown))
        return [opt.text for opt in select.options]


class InputsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/inputs"

    _number_input = (By.CSS_SELECTOR, "input[type='number']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_number(self, value):
        self.type_text(*self._number_input, str(value))

    def get_input_value(self):
        return self.find(*self._number_input).get_attribute("value")
