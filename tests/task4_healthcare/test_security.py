import pytest
from pages.healthcare.security_page import SecurityPage


@pytest.mark.security
class TestSecurityPrivacy:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = SecurityPage(driver)

    def test_page_uses_https(self, driver):
        self.page.navigate_to_public_page()
        assert self.page.check_page_is_secure()

    def test_no_http_links_on_page(self, driver):
        self.page.navigate_to_public_page()
        assert self.page.check_no_http_links()

    def test_no_exposed_ssn_pattern(self, driver):
        self.page.navigate_to_public_page()
        ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"
        matches = self.page.get_page_contains_sensitive_data(ssn_pattern)
        assert len(matches) == 0

    def test_no_exposed_credit_card_pattern(self, driver):
        self.page.navigate_to_public_page()
        cc_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
        matches = self.page.get_page_contains_sensitive_data(cc_pattern)
        assert len(matches) == 0

    def test_private_page_requires_login(self, driver):
        self.page.navigate_to_private_page()
        assert self.page.is_redirected_to_login()

    def test_password_strength_weak(self, driver):
        self.page.driver.get("https://www.carehealthusa.com/register")
        strength = self.page.get_password_strength("abc")
        assert "weak" in strength.lower() or "fair" in strength.lower()

    def test_password_strength_strong(self, driver):
        self.page.driver.get("https://www.carehealthusa.com/register")
        strength = self.page.get_password_strength("Str0ng!Pass#2026")
        assert "strong" in strength.lower()

    def test_password_requirements_displayed(self, driver):
        self.page.driver.get("https://www.carehealthusa.com/register")
        reqs = self.page.get_password_requirements()
        assert len(reqs) > 0
