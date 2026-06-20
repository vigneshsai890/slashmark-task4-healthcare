import pytest
from pages.healthcare.appointment_page import DropdownPage, InputsPage


class TestDropdown:
    @pytest.mark.smoke
    @pytest.mark.healthcare
    def test_dropdown_options_displayed(self, driver):
        page = DropdownPage(driver)
        page.open()
        options = page.get_all_options()
        assert len(options) == 3
        assert "Please select an option" in options[0]

    @pytest.mark.healthcare
    def test_select_option_1(self, driver):
        page = DropdownPage(driver)
        page.open()
        page.select_by_text("Option 1")
        assert page.get_selected_text() == "Option 1"

    @pytest.mark.healthcare
    def test_select_option_2(self, driver):
        page = DropdownPage(driver)
        page.open()
        page.select_by_value("2")
        assert page.get_selected_text() == "Option 2"


class TestInputs:
    @pytest.mark.smoke
    @pytest.mark.healthcare
    def test_enter_number(self, driver):
        page = InputsPage(driver)
        page.open()
        page.enter_number(42)
        assert page.get_input_value() == "42"

    @pytest.mark.healthcare
    def test_enter_negative_number(self, driver):
        page = InputsPage(driver)
        page.open()
        page.enter_number(-10)
        assert page.get_input_value() == "-10"
