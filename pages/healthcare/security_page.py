from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import re


class SecurityPage(BasePage):
    GOOGLE_URL = "https://www.google.com"
    LOGIN_URL = "https://the-internet.herokuapp.com/login"

    def open_google(self):
        self.driver.get(self.GOOGLE_URL)
        return self

    def open_login(self):
        self.driver.get(self.LOGIN_URL)
        return self

    def is_https(self):
        return self.driver.current_url.startswith("https://")

    def get_all_links(self):
        links = self.find_all(By.TAG_NAME, "a")
        return [link.get_attribute("href") for link in links if link.get_attribute("href")]

    def has_http_links(self):
        links = self.get_all_links()
        return any(link.startswith("http://") for link in links if link)

    def get_page_source(self):
        return self.driver.page_source

    def contains_email_pattern(self):
        source = self.get_page_source()
        return bool(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', source))

    def contains_ssn_pattern(self):
        source = self.get_page_source()
        return bool(re.search(r'\b\d{3}-\d{2}-\d{4}\b', source))

    def contains_phone_pattern(self):
        source = self.get_page_source()
        return bool(re.search(r'\(\d{3}\)\s*\d{3}-\d{4}', source))

    def get_cookies(self):
        return self.driver.get_cookies()

    def has_secure_cookies(self):
        cookies = self.get_cookies()
        if not cookies:
            return True
        secure_count = sum(1 for c in cookies if c.get("secure", False))
        return secure_count > 0
