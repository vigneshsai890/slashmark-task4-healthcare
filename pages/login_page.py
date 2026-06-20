from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.practo.com/login"

    USERNAME = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.CLASS_NAME, "error-message")

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.type(*self.USERNAME, email)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def get_error(self):
        return self.get_text(*self.ERROR_MSG)
