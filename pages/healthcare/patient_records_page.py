from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TablesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/tables"

    _table1_rows = (By.CSS_SELECTOR, "#table1 tbody tr")
    _table2_rows = (By.CSS_SELECTOR, "#table2 tbody tr")
    _table1_headers = (By.CSS_SELECTOR, "#table1 thead th")

    def open(self):
        self.driver.get(self.URL)
        return self

    def get_table1_row_count(self):
        return len(self.find_all(*self._table1_rows))

    def get_table2_row_count(self):
        return len(self.find_all(*self._table2_rows))

    def get_headers(self):
        headers = self.find_all(*self._table1_headers)
        return [h.text for h in headers]

    def get_row_data(self, row_index):
        rows = self.find_all(*self._table1_rows)
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_all_last_names(self):
        rows = self.find_all(*self._table1_rows)
        return [row.find_elements(By.TAG_NAME, "td")[0].text for row in rows]

    def get_all_emails(self):
        rows = self.find_all(*self._table1_rows)
        return [row.find_elements(By.TAG_NAME, "td")[2].text for row in rows]

    def get_due_amounts(self):
        rows = self.find_all(*self._table1_rows)
        return [row.find_elements(By.TAG_NAME, "td")[3].text for row in rows]
