import pytest
from pages.healthcare.patient_records_page import TablesPage


class TestPatientRecords:
    @pytest.mark.smoke
    @pytest.mark.healthcare
    def test_table1_has_rows(self, driver):
        page = TablesPage(driver)
        page.open()
        assert page.get_table1_row_count() == 4

    @pytest.mark.healthcare
    def test_table2_has_rows(self, driver):
        page = TablesPage(driver)
        page.open()
        assert page.get_table2_row_count() == 4

    @pytest.mark.healthcare
    def test_table_headers(self, driver):
        page = TablesPage(driver)
        page.open()
        headers = page.get_headers()
        assert "Last Name" in headers
        assert "First Name" in headers
        assert "Email" in headers
        assert "Due" in headers

    @pytest.mark.healthcare
    def test_first_row_data(self, driver):
        page = TablesPage(driver)
        page.open()
        row = page.get_row_data(0)
        assert row[0] == "Smith"
        assert row[1] == "John"
        assert "jsmith@" in row[2]

    @pytest.mark.healthcare
    def test_all_last_names(self, driver):
        page = TablesPage(driver)
        page.open()
        names = page.get_all_last_names()
        assert "Smith" in names
        assert "Bach" in names
        assert "Conway" in names
        assert "Conway" in names
