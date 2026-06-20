import pytest
from pages.patient_records_page import PatientRecordsPage
from faker import Faker

fake = Faker()


class TestPatientRecords:

    def test_add_new_patient_record(self, driver):
        page = PatientRecordsPage(driver)
        page.open()
        initial = page.get_row_count()
        page.add_patient(
            fake.first_name(), fake.last_name(),
            fake.email(), "35", "Cardiology"
        )
        assert page.get_row_count() > initial, "New patient record should appear in table"

    def test_search_patient_by_name(self, driver):
        page = PatientRecordsPage(driver)
        page.open()
        page.add_patient("SearchTest", "Patient", "search@test.com", "40", "Neurology")
        page.search_patient("SearchTest")
        assert page.get_row_count() >= 1, "Search should return matching patient"

    def test_search_no_results(self, driver):
        page = PatientRecordsPage(driver)
        page.open()
        page.search_patient("ZZZNONEXISTENT999")
        assert page.get_row_count() == 0, "No results for unknown patient"

    def test_patient_record_fields_required(self, driver):
        page = PatientRecordsPage(driver)
        page.open()
        page.click(*page.ADD_BTN)
        page.click(*page.SUBMIT)
        # form validation — modal should still be open
        assert page.is_visible(*page.FIRSTNAME), "Required field errors should show"

    def test_multiple_patients_added(self, driver):
        page = PatientRecordsPage(driver)
        page.open()
        for i in range(3):
            page.add_patient(
                f"Patient{i}", f"Test{i}",
                f"patient{i}@hospital.com", str(30 + i), "General"
            )
        assert page.get_row_count() >= 3
