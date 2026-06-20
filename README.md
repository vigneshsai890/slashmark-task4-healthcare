# Task 4 — Healthcare Website Automation Testing

Automated test suite for healthcare-style web interactions using Python + Selenium + pytest. Covers authentication, form interactions, table data, and security validations against real, publicly available demo sites.

## What's Tested

- **Login & Authentication** — Valid/invalid login, flash messages, form validation
- **Form Interactions** — Dropdown selections, numeric inputs, form validation
- **Patient Records (Tables)** — Table display, row counts, data extraction, headers
- **Security & Privacy** — HTTPS validation, no exposed data, secure cookies

## Target Sites

- [The Internet - Login](https://the-internet.herokuapp.com/login) — Login form with tomsmith / SuperSecretPassword!
- [The Internet - Dropdown](https://the-internet.herokuapp.com/dropdown) — Dropdown selection tests
- [The Internet - Inputs](https://the-internet.herokuapp.com/inputs) — Numeric input tests
- [The Internet - Tables](https://the-internet.herokuapp.com/tables) — Table data display tests
- [Google](https://www.google.com) — HTTPS and security validation

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# By category
pytest -m smoke
pytest -m healthcare
pytest -m security

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Tech Stack

- Python 3 + Selenium 4 + pytest
- Page Object Model design pattern
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
