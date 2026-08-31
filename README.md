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
│   └── part1_flaky_test_analysis.md
│
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt