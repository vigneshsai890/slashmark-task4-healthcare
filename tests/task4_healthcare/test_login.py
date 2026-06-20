import pytest
from pages.healthcare.login_page import LoginPage


class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.healthcare
    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        assert "/secure" in page.current_url
        assert "You logged into a secure area!" in page.get_flash_message()

    @pytest.mark.smoke
    @pytest.mark.healthcare
    def test_invalid_username(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("wronguser", "SuperSecretPassword!")
        message = page.get_flash_message()
        assert "Your username is invalid!" in message

    @pytest.mark.healthcare
    def test_invalid_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "wrongpassword")
        message = page.get_flash_message()
        assert "Your password is invalid!" in message

    @pytest.mark.healthcare
    def test_empty_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("", "")
        message = page.get_flash_message()
        assert "Your username is invalid!" in message

    @pytest.mark.healthcare
    def test_login_form_displayed(self, driver):
        page = LoginPage(driver)
        page.open()
        assert page.is_login_form_displayed()
