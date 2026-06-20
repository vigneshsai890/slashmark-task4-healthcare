from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PatientRecordsPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    SEARCH_BOX = (By.ID, "patient-search")
    SEARCH_BTN = (By.ID, "search-btn")

    PATIENT_TABLE = (By.CSS_SELECTOR, "table.patient-table tbody tr")
    PATIENT_NAME = (By.CSS_SELECTOR, "td.patient-name")
    PATIENT_ID = (By.CSS_SELECTOR, "td.patient-id")
    PATIENT_DOB = (By.CSS_SELECTOR, "td.patient-dob")

    RECORD详情BTN = (By.CSS_SELECTOR, ".view-record-btn")
    RECORD详情SECTION = (By.CSS_SELECTOR, ".patient-detail-section")

    VITALS_TABLE = (By.CSS_SELECTOR, ".vitals-table")
    MEDICATION_LIST = (By.CSS_SELECTOR, ".medication-item")
    ALLERGY_LIST = (By.CSS_SELECTOR, ".allergy-item")
    VISIT_HISTORY = (By.CSS_SELECTOR, ".visit-entry")

    def search_patient(self, name):
        self.type_text(*self.SEARCH_BOX, name)
        self.click(*self.SEARCH_BTN)
        return self

    def get_patient_count(self):
        try:
            return len(self.find_all(*self.PATIENT_TABLE))
        except:
            return 0

    def get_patient_names(self):
        elements = self.find_all(*self.PATIENT_NAME)
        return [el.text for el in elements]

    def click_view_record(self, index=0):
        btns = self.find_all(*self.RECORD详情BTN)
        btns[index].click()
        return self

    def is_record_detail_visible(self):
        return self.is_visible(*self.RECORD详情SECTION)

    def get_vitals(self):
        table = self.find(*self.VITALS_TABLE)
        rows = table.find_elements(By.TAG_NAME, "tr")
        vitals = {}
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 2:
                vitals[cols[0].text.strip()] = cols[1].text.strip()
        return vitals

    def get_medication_count(self):
        try:
            return len(self.find_all(*self.MEDICATION_LIST))
        except:
            return 0

    def get_allergy_count(self):
        try:
            return len(self.find_all(*self.ALLERGY_LIST))
        except:
            return 0

    def get_visit_count(self):
        try:
            return len(self.find_all(*self.VISIT_HISTORY))
        except:
            return 0
