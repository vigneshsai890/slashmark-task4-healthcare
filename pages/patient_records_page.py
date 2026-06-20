from selenium.webdriver.common.by import By
from .base_page import BasePage


class PatientRecordsPage(BasePage):
    URL = "https://demoqa.com/webtables"

    ADD_BTN    = (By.ID, "addNewRecordButton")
    FIRSTNAME  = (By.ID, "firstName")
    LASTNAME   = (By.ID, "lastName")
    EMAIL      = (By.ID, "userEmail")
    AGE        = (By.ID, "age")
    SALARY     = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT     = (By.ID, "submit")
    SEARCH     = (By.ID, "searchBox")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")

    def open(self):
        self.driver.get(self.URL)

    def add_patient(self, first, last, email, age, dept):
        self.click(*self.ADD_BTN)
        self.type(*self.FIRSTNAME, first)
        self.type(*self.LASTNAME, last)
        self.type(*self.EMAIL, email)
        self.type(*self.AGE, age)
        self.type(*self.SALARY, "0")
        self.type(*self.DEPARTMENT, dept)
        self.click(*self.SUBMIT)

    def search_patient(self, query):
        self.type(*self.SEARCH, query)

    def get_row_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return sum(1 for r in rows if r.text.strip())
