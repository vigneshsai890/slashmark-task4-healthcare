from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class AppointmentPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    FIRSTNAME = (By.ID, "firstName")
    LASTNAME  = (By.ID, "lastName")
    EMAIL     = (By.ID, "userEmail")
    MOBILE    = (By.ID, "userNumber")
    DOB       = (By.ID, "dateOfBirthInput")
    SUBJECT   = (By.ID, "subjectsInput")
    SUBMIT    = (By.ID, "submit")
    SUCCESS   = (By.ID, "example-modal-sizes-title-lg")

    def open(self):
        self.driver.get(self.URL)

    def fill_appointment(self, first, last, email, mobile):
        self.type(*self.FIRSTNAME, first)
        self.type(*self.LASTNAME, last)
        self.type(*self.EMAIL, email)
        self.type(*self.MOBILE, mobile)

    def submit(self):
        self.driver.execute_script("arguments[0].click();", self.find(*self.SUBMIT))

    def is_success(self):
        return self.is_visible(*self.SUCCESS)
