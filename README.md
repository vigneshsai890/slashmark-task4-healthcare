# Task 4 — Healthcare Website Automation Testing

Automated test suite for healthcare websites using Python + Selenium + pytest. Covers appointment scheduling, patient records, role-based access, and security/privacy validations.

## What's Tested

- **Appointment Scheduling** — Book, view, cancel appointments with various providers
- **Patient Records** — View patient info, validate data fields, search patients
- **Role-Based Access** — Doctor vs patient vs admin permissions
- **Security & Privacy** — HIPAA-style checks, session timeout, secure navigation, data masking
- **Login & Authentication** — Valid/invalid login, password policies, account lockout

## Target Sites

- [Patient Portal Demo](https://demo.patientportal.com) (mock)
- [ACA Healthcare Demo](https://www.carehealthusa.com) (demo forms)
- Custom mock endpoints for security testing

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
- Pillow for screenshot-based validation
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
