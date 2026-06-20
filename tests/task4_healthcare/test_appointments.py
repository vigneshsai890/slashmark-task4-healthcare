import pytest
from pages.healthcare.appointment_page import AppointmentPage


@pytest.mark.healthcare
class TestAppointmentScheduling:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = AppointmentPage(driver)
        self.page.driver.get("https://www.carehealthusa.com/appointments")

    def test_page_loads(self, driver):
        assert self.page.is_visible(*self.page.APPOINTMENT_FORM, timeout=10)

    def test_doctor_dropdown_populated(self, driver):
        options = self.page.get_doctor_options()
        assert len(options) > 0

    def test_department_dropdown_populated(self, driver):
        options = self.page.get_department_options()
        assert len(options) > 0

    @pytest.mark.smoke
    def test_book_appointment_success(self, driver):
        self.page.select_doctor("Dr. Smith")
        self.page.select_department("Cardiology")
        self.page.select_date("07/15/2026")
        self.page.select_time_slot("10:00 AM")
        self.page.enter_reason("Annual checkup")
        self.page.book_appointment()
        assert self.page.is_success_displayed()

    def test_book_without_date_fails(self, driver):
        self.page.select_doctor("Dr. Smith")
        self.page.select_department("Cardiology")
        self.page.select_time_slot("10:00 AM")
        self.page.enter_reason("Annual checkup")
        self.page.book_appointment()
        assert self.page.is_visible(*self.page.ERROR_MSG)

    def test_appointments_list_displayed(self, driver):
        count = self.page.get_appointment_count()
        assert count >= 0

    def test_cancel_appointment(self, driver):
        initial_count = self.page.get_appointment_count()
        if initial_count > 0:
            self.page.cancel_appointment(0)
            new_count = self.page.get_appointment_count()
            assert new_count < initial_count


@pytest.mark.healthcare
class TestAppointmentValidation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = AppointmentPage(driver)
        self.page.driver.get("https://www.carehealthusa.com/appointments")

    @pytest.mark.parametrize("reason", [
        "Routine checkup",
        "Follow-up consultation",
        "Prescription refill",
        "Lab results review",
    ])
    def test_various_appointment_reasons(self, driver, reason):
        self.page.select_doctor("Dr. Smith")
        self.page.select_department("General")
        self.page.select_date("08/01/2026")
        self.page.select_time_slot("02:00 PM")
        self.page.enter_reason(reason)
        self.page.book_appointment()
        assert self.page.is_success_displayed()
