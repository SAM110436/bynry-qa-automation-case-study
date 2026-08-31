import os

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.mobile
def test_project_access_on_mobile():
    """
    BrowserStack mobile validation.

    This test demonstrates the intended approach for validating
    the project on a real mobile device through BrowserStack.
    """

    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if not username or not access_key:
        pytest.skip(
            "BrowserStack credentials are not configured."
        )

    capabilities = {
        "browser": "Chrome",
        "device": "Samsung Galaxy S22",
        "os": "android",
        "os_version": "12.0",
        "name": "Project Mobile Accessibility",
        "build": "Bynry QA Automation Case Study",
    }

    browserstack_url = (
        "wss://cdp.browserstack.com/playwright"
        f"?caps={capabilities}"
    )

    with sync_playwright() as p:
        browser = p.chromium.connect(
            browserstack_url
        )

        context = browser.new_context(
            viewport={
                "width": 390,
                "height": 844,
            }
        )

        page = context.new_page()

        try:
            page.goto(
                "https://app.workflowpro.com/login",
                wait_until="domcontentloaded",
            )

            expect(
                page.locator("#email")
            ).to_be_visible(timeout=15_000)

            # Credentials should come from CI/CD secrets.
            page.locator("#email").fill(
                os.getenv("COMPANY1_EMAIL", "")
            )

            page.locator("#password").fill(
                os.getenv("COMPANY1_PASSWORD", "")
            )

            page.locator("#login-btn").click()

            expect(page).to_have_url(
                "https://app.workflowpro.com/dashboard",
                timeout=15_000,
            )

            expect(
                page.locator(".welcome-message")
            ).to_be_visible(timeout=15_000)

        finally:
            context.close()
            browser.close()