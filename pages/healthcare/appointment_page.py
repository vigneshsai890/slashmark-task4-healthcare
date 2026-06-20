from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class AppointmentPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    APPOINTMENT_FORM = (By.ID, "appointment-form")

    PATIENT_NAME = (By.ID, "patient-name")
    DOCTOR_DROPDOWN = (By.ID, "doctor-select")
    DEPARTMENT_DROPDOWN = (By.ID, "department-select")
    DATE_PICKER = (By.ID, "appointment-date")
    TIME_SLOT = (By.ID, "time-slot")
    REASON = (By.ID, "reason")
    SUBMIT_BTN = (By.ID, "book-appointment")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".success-message")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message")

    APPOINTMENT_LIST = (By.CSS_SELECTOR, ".appointment-card")
    CANCEL_BTN = (By.CSS_SELECTOR, ".cancel-appointment-btn")
    CONFIRM_CANCEL = (By.CSS_SELECTOR, ".confirm-cancel")

    def get_page_title_text(self):
        return self.get_text(*self.PAGE_TITLE)

    def select_doctor(self, doctor_name):
        Select(self.find(*self.DOCTOR_DROPDOWN)).select_by_visible_text(doctor_name)
        return self

    def select_department(self, department):
        Select(self.find(*self.DEPARTMENT_DROPDOWN)).select_by_visible_text(department)
        return self

    def select_date(self, date):
        self.type_text(*self.DATE_PICKER, date)
        return self

    def select_time_slot(self, time_text):
        Select(self.find(*self.TIME_SLOT)).select_by_visible_text(time_text)
        return self

    def enter_reason(self, reason):
        self.type_text(*self.REASON, reason)
        return self

    def book_appointment(self):
        self.click(*self.SUBMIT_BTN)
        return self

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MSG)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MSG)

    def is_success_displayed(self):
        return self.is_visible(*self.SUCCESS_MSG, timeout=5)

    def get_appointment_count(self):
        try:
            return len(self.find_all(*self.APPOINTMENT_LIST))
        except:
            return 0

    def cancel_appointment(self, index=0):
        btns = self.find_all(*self.CANCEL_BTN)
        btns[index].click()
        self.click(*self.CONFIRM_CANCEL)

    def get_doctor_options(self):
        select = Select(self.find(*self.DOCTOR_DROPDOWN))
        return [o.text for o in select.options if o.text]

    def get_department_options(self):
        select = Select(self.find(*self.DEPARTMENT_DROPDOWN))
        return [o.text for o in select.options if o.text]
