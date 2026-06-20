import pytest
from pages.appointment_page import AppointmentPage
from faker import Faker

fake = Faker()


class TestAppointmentScheduling:

    def test_valid_appointment_booking(self, driver):
        page = AppointmentPage(driver)
        page.open()
        page.fill_appointment(
            fake.first_name(), fake.last_name(),
            fake.email(), "9876543210"
        )
        page.submit()
        assert page.is_success(), "Appointment submission should show success modal"

    def test_appointment_missing_required_fields(self, driver):
        page = AppointmentPage(driver)
        page.open()
        page.submit()
        # form should not submit — URL stays same or error shown
        assert "automation-practice-form" in driver.current_url

    def test_appointment_invalid_mobile(self, driver):
        page = AppointmentPage(driver)
        page.open()
        page.fill_appointment(
            fake.first_name(), fake.last_name(),
            fake.email(), "abc"  # invalid mobile
        )
        page.submit()
        assert not page.is_success(), "Invalid mobile should not trigger success"

    def test_appointment_invalid_email(self, driver):
        page = AppointmentPage(driver)
        page.open()
        page.fill_appointment(
            fake.first_name(), fake.last_name(),
            "notanemail", "9876543210"
        )
        page.submit()
        assert not page.is_success(), "Invalid email should not trigger success"

    def test_appointment_page_title(self, driver):
        page = AppointmentPage(driver)
        page.open()
        assert "ToolsQA" in driver.title
