from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    _username = (By.ID, "username")
    _password = (By.ID, "password")
    _submit = (By.CSS_SELECTOR, "button[type='submit']")
    _flash = (By.ID, "flash")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self._username, username)
        self.type_text(*self._password, password)
        self.click(*self._submit)

    def get_flash_message(self):
        return self.get_text(*self._flash)

    def is_login_form_displayed(self):
        return self.is_visible(*self._username)
