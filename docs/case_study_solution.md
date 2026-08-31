# Bynry QA Automation Engineering Intern Case Study

## B2B SaaS Platform Testing - Multi-Platform Automation

**Candidate:** Sameer Patil

---

# Part 1: Debugging Flaky Test Code

## 1. Flakiness Issues Identified

The original login test can fail intermittently for several reasons:

1. **No explicit synchronization**
   - `page.goto()` does not guarantee that all application data and dynamic dashboard elements have finished loading.
   - The test immediately interacts with elements after navigation.

2. **Hard-coded selectors**
   - Selectors such as `#email`, `#password`, and `#login-btn` depend on implementation details.
   - If the UI changes, the test can fail.

3. **No handling for dynamic dashboard loading**
   - The dashboard contains dynamically loaded elements.
   - The test checks the URL and welcome message immediately after clicking login.

4. **Immediate URL assertion**
   - `assert page.url == ...` can execute before navigation has completed.

5. **No handling for 2FA**
   - Some users require 2FA.
   - The original test assumes login always completes in a single step.

6. **Different tenant loading times**
   - Company1 and Company2 may require different amounts of time to load their data.

7. **CI/CD environment differences**
   - CI machines may have slower CPU, network, or disk performance.
   - Tests may behave differently from a developer's local machine.

8. **Browser and viewport differences**
   - CI may execute tests against different browsers and screen sizes.
   - Responsive layouts can affect element visibility and interaction.

9. **No failure diagnostics**
   - The original test does not capture screenshots, traces, or useful logs when a failure occurs.

10. **Browser lifecycle is manually managed**
   - Each test creates and closes its own browser.
   - pytest fixtures provide cleaner and more reusable lifecycle management.

---

## 2. Root Causes in CI/CD

Flaky tests frequently occur in CI/CD because CI environments are less predictable than local development machines.

Common causes include:

- slower execution environments
- network latency
- dynamic application loading
- browser differences
- responsive layout changes
- race conditions
- asynchronous API calls
- authentication/2FA delays
- parallel test execution
- shared test data
- environment instability

The main issue with the original test is that it relies on timing assumptions instead of waiting for observable application states.

---

## 3. Stabilization Approach

The corrected implementation uses:

- pytest fixtures
- Playwright's built-in auto-waiting
- locator-based assertions
- explicit waits for important application states
- configurable credentials
- reusable Page Object classes
- screenshots/traces through pytest configuration
- environment variables instead of hard-coded secrets

Example:

```python
def test_user_login(app_page):
    login_page = LoginPage(app_page)

    login_page.open()
    login_page.login(
        email=settings.COMPANY1_EMAIL,
        password=settings.COMPANY1_PASSWORD,
    )

    expect(app_page).to_have_url(
        re.compile(r".*/dashboard")
    )

    expect(
        app_page.locator(".welcome-message")
    ).to_be_visible()