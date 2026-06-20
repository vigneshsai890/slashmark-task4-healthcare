import pytest
from pages.healthcare.login_page import HealthcareLoginPage


@pytest.mark.healthcare
class TestHealthcareLogin:
    def test_page_loads(self, driver):
        page = HealthcareLoginPage(driver).open()
        assert page.is_visible(*page.USERNAME, timeout=10)

    @pytest.mark.parametrize("username,password", [
        ("doctor_smith", "SecurePass123!"),
        ("nurse_jones", "NursePass456!"),
        ("admin_user", "AdminPass789!"),
    ])
    def test_valid_login(self, driver, username, password):
        page = HealthcareLoginPage(driver).open()
        page.login(username, password)
        assert not page.is_error_displayed()

    @pytest.mark.parametrize("username,password,expected_error", [
        ("invalid_user", "SecurePass123!", "Invalid username or password"),
        ("doctor_smith", "wrongpass", "Invalid username or password"),
        ("", "SecurePass123!", "Username is required"),
        ("doctor_smith", "", "Password is required"),
    ])
    def test_invalid_login(self, driver, username, password, expected_error):
        page = HealthcareLoginPage(driver).open()
        page.login(username, password)
        assert expected_error in page.get_error()

    def test_remember_me_option(self, driver):
        page = HealthcareLoginPage(driver).open()
        assert not page.is_remember_me_checked()

    def test_forgot_password_link(self, driver):
        page = HealthcareLoginPage(driver).open()
        page.click_forgot_password()
        assert "forgot" in driver.current_url.lower() or "reset" in driver.current_url.lower()
