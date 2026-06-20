from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import re


class SecurityPage(BasePage):
    SECURE_HEADER = (By.CSS_SELECTOR, ".secure-indicator")
    SESSION_TIMEOUT_MSG = (By.CSS_SELECTOR, ".session-timeout")
    PUBLIC_URL = "https://www.carehealthusa.com/public"
    PRIVATE_URL = "https://www.carehealthusa.com/patient/dashboard"

    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_STRENGTH = (By.CSS_SELECTOR, ".password-strength")
    PASSWORD_REQUIREMENTS = (By.CSS_SELECTOR, ".password-req li")

    def check_page_is_secure(self):
        return self.driver.current_url.startswith("https://")

    def get_page_contains_sensitive_data(self, pattern):
        source = self.driver.page_source
        matches = re.findall(pattern, source)
        return matches

    def check_no_http_links(self):
        links = self.find_all(By.TAG_NAME, "a")
        http_links = [l for l in links if l.get_attribute("href", "").startswith("http://")]
        return len(http_links) == 0

    def get_password_strength(self, password):
        self.type_text(*self.PASSWORD_FIELD, password)
        return self.get_text(*self.PASSWORD_STRENGTH)

    def get_password_requirements(self):
        elements = self.find_all(*self.PASSWORD_REQUIREMENTS)
        return [el.text for el in elements]

    def navigate_to_public_page(self):
        self.driver.get(self.PUBLIC_URL)

    def navigate_to_private_page(self):
        self.driver.get(self.PRIVATE_URL)

    def is_redirected_to_login(self):
        return "login" in self.driver.current_url.lower()

    def check_session_cookie_secure(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie.get("name") == "session":
                return cookie.get("secure", False)
        return False
