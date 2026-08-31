# Bynry QA Automation Case Study

## Overview

This repository contains my solution for the Bynry QA Automation Engineering Intern case study.

The solution demonstrates:

- Playwright UI automation
- pytest-based test execution
- Flaky test analysis and stabilization
- Page Object Model
- API automation
- Multi-tenant testing
- Tenant isolation validation
- Mobile testing approach
- BrowserStack integration concepts
- CI/CD-oriented configuration
- Test data and environment configuration

---
## Test Execution Status

The test framework was successfully configured and executed locally using pytest.

The external WorkFlow Pro environment currently returns an SSL certificate error (`ERR_CERT_COMMON_NAME_INVALID`), so the live UI/API tests cannot be fully validated against the external application from the local environment.

Latest local execution:

- **Tests collected:** 4
- **Passed:** 0
- **Failed:** 3
- **Skipped:** 1
- **UI failures:** External WorkFlow Pro SSL/certificate issue
- **API failure:** External WorkFlow Pro API connection issue
- **Mobile test:** Skipped because BrowserStack credentials were unavailable

The test execution report documents these environment limitations. No tests were artificially marked as passed.

# Project Structure

```text
bynry-qa-automation-case-study/
│
├── framework/
│   ├── api/
│   │   ├── __init__.py
│   │   └── client.py
│   ├── browserstack/
│   │   └── browserstack_config.py
│   ├── config/
│   │   └── __init__.py
│   ├── fixtures/
│   │   └── conftest.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   └── project_page.py
│   ├── utils/
│   ├── __init__.py
│   └── settings.py
│
├── tests/
│   ├── part1_flaky_login/
│   │   └── test_login.py
│   └── part3_integration/
│       ├── test_project_creation.py
│       └── test_mobile_project.py
│
├── test_data/
├── docs/
│   ├── part1_flaky_test_analysis.md
│   ├── case_study_solution.md
│   └── test_execution_report.md
│
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt