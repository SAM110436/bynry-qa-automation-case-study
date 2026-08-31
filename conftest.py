import pytest
from playwright.sync_api import Browser, Page, Playwright

from framework.settings import settings


@pytest.fixture
def app_page(playwright: Playwright, browser: Browser) -> Page:
    """Create a fresh browser page for an application test."""

    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
    )

    page = context.new_page()

    yield page

    context.close()


@pytest.fixture
def tenant_context() -> dict[str, str]:
    """Provide tenant configuration for tests."""

    return {
        "company1": settings.COMPANY1_EMAIL,
        "company2": settings.COMPANY2_EMAIL,
    }