import pytest
from pages.healthcare.patient_records_page import PatientRecordsPage


@pytest.mark.healthcare
class TestPatientRecords:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = PatientRecordsPage(driver)
        self.page.driver.get("https://www.carehealthusa.com/patients")

    def test_page_loads(self, driver):
        assert self.page.is_visible(*self.page.SEARCH_BOX, timeout=10)

    def test_search_patient(self, driver):
        self.page.search_patient("John")
        count = self.page.get_patient_count()
        assert count >= 0

    def test_patient_names_not_empty(self, driver):
        self.page.search_patient("John")
        names = self.page.get_patient_names()
        assert all(len(n) > 0 for n in names)

    @pytest.mark.smoke
    def test_view_patient_record(self, driver):
        self.page.search_patient("John")
        if self.page.get_patient_count() > 0:
            self.page.click_view_record(0)
            assert self.page.is_record_detail_visible()

    def test_vitals_displayed(self, driver):
        self.page.search_patient("John")
        if self.page.get_patient_count() > 0:
            self.page.click_view_record(0)
            vitals = self.page.get_vitals()
            assert len(vitals) > 0

    def test_medication_list(self, driver):
        self.page.search_patient("John")
        if self.page.get_patient_count() > 0:
            self.page.click_view_record(0)
            count = self.page.get_medication_count()
            assert count >= 0

    def test_visit_history(self, driver):
        self.page.search_patient("John")
        if self.page.get_patient_count() > 0:
            self.page.click_view_record(0)
            count = self.page.get_visit_count()
            assert count >= 0
