import pytest
from pages.healthcare.security_page import SecurityPage


class TestSecurity:
    @pytest.mark.smoke
    @pytest.mark.security
    def test_google_uses_https(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert page.is_https()

    @pytest.mark.security
    def test_login_page_uses_https(self, driver):
        page = SecurityPage(driver)
        page.open_login()
        assert page.is_https()

    @pytest.mark.security
    def test_no_http_links_on_google(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert not page.has_http_links()

    @pytest.mark.security
    def test_no_exposed_emails(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert not page.contains_email_pattern()

    @pytest.mark.security
    def test_no_exposed_ssns(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert not page.contains_ssn_pattern()

    @pytest.mark.security
    def test_no_exposed_phone_numbers(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert not page.contains_phone_pattern()

    @pytest.mark.security
    def test_cookies_are_secure(self, driver):
        page = SecurityPage(driver)
        page.open_google()
        assert page.has_secure_cookies()
