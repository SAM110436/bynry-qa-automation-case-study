import os

import pytest
from playwright.sync_api import sync_playwright, expect

from framework.browserstack.browserstack_config import (
    get_browserstack_ws_endpoint,
)


@pytest.mark.mobile
def test_project_access_on_mobile():
    """
    Validate project accessibility on a real Android device
    through BrowserStack.

    This test requires BrowserStack credentials and a reachable
    WorkFlow Pro test environment.
    """

    if not os.getenv("BROWSERSTACK_USERNAME") or not os.getenv(
        "BROWSERSTACK_ACCESS_KEY"
    ):
        pytest.skip(
            "BrowserStack credentials are not configured."
        )

    email = os.getenv("COMPANY1_EMAIL")
    password = os.getenv("COMPANY1_PASSWORD")

    if not email or not password:
        pytest.skip(
            "Company 1 test credentials are not configured."
        )

    with sync_playwright() as p:
        browser = p.chromium.connect(
            get_browserstack_ws_endpoint(
                device="Samsung Galaxy S22",
                os_name="android",
                os_version="12.0",
            )
        )

        page = browser.new_page()

        try:
            page.goto(
                "https://app.workflowpro.com/login",
                wait_until="domcontentloaded",
                timeout=30_000,
            )

            expect(
                page.locator("#email")
            ).to_be_visible(timeout=15_000)

            page.locator("#email").fill(email)
            page.locator("#password").fill(password)
            page.locator("#login-btn").click()

            expect(page).to_have_url(
                "https://app.workflowpro.com/dashboard",
                timeout=20_000,
            )

            expect(
                page.locator(".welcome-message")
            ).to_be_visible(timeout=15_000)

        finally:
            browser.close()