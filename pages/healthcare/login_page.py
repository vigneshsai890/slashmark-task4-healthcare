from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HealthcareLoginPage(BasePage):
    URL = "https://www.carehealthusa.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    REMEMBER_ME = (By.ID, "remember-me")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME, username)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        return self

    def get_error(self):
        return self.get_text(*self.ERROR_MSG)

    def is_error_displayed(self):
        return self.is_visible(*self.ERROR_MSG)

    def click_forgot_password(self):
        self.click(*self.FORGOT_PASSWORD_LINK)

    def is_remember_me_checked(self):
        return self.find(*self.REMEMBER_ME).is_selected()
