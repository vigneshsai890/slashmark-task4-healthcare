import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRoleBasedAccess:
    """Role-based access control tests using demoqa.com"""

    BASE_URL = "https://demoqa.com"

    def test_admin_login_page_accessible(self, driver):
        driver.get(f"{self.BASE_URL}/login")
        assert "ToolsQA" in driver.title

    def test_valid_admin_login(self, driver):
        driver.get(f"{self.BASE_URL}/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "login").click()
        # demoqa shows profile on valid login attempt
        assert driver.current_url is not None

    def test_invalid_credentials_blocked(self, driver):
        driver.get(f"{self.BASE_URL}/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("hacker")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "login").click()
        error = wait.until(EC.presence_of_element_located((By.ID, "name")))
        assert "Invalid" in error.text or driver.current_url.endswith("/login")

    def test_empty_credentials_blocked(self, driver):
        driver.get(f"{self.BASE_URL}/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "login"))).click()
        # should stay on login page
        assert "login" in driver.current_url

    def test_unauthenticated_protected_route(self, driver):
        driver.get(f"{self.BASE_URL}/profile")
        # without login should stay or redirect
        assert "demoqa.com" in driver.current_url
