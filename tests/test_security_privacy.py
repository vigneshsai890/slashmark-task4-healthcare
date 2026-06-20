import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSecurityPrivacy:
    """Security and privacy validation tests for healthcare context"""

    def test_https_connection(self, driver):
        driver.get("https://demoqa.com")
        assert driver.current_url.startswith("https://"), "Site must use HTTPS"

    def test_password_field_masked(self, driver):
        driver.get("https://demoqa.com/login")
        wait = WebDriverWait(driver, 10)
        pwd = wait.until(EC.presence_of_element_located((By.ID, "password")))
        assert pwd.get_attribute("type") == "password", "Password must be masked"

    def test_sql_injection_in_search(self, driver):
        driver.get("https://demoqa.com/webtables")
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
        search.send_keys("' OR '1'='1")
        rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        visible = [r for r in rows if r.text.strip()]
        # injection should return 0 results, not all records
        assert len(visible) == 0, "SQL injection should not return all records"

    def test_xss_in_input_field(self, driver):
        driver.get("https://demoqa.com/webtables")
        wait = WebDriverWait(driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_btn.click()
        first = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
        first.send_keys("<script>alert('xss')</script>")
        # check no alert fires
        try:
            WebDriverWait(driver, 2).until(EC.alert_is_present())
            driver.switch_to.alert.dismiss()
            assert False, "XSS script should not execute"
        except Exception:
            assert True

    def test_sensitive_data_not_in_url(self, driver):
        driver.get("https://demoqa.com/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("testpass")
        driver.find_element(By.ID, "login").click()
        assert "password" not in driver.current_url, "Password must not appear in URL"
        assert "testpass" not in driver.current_url
