import os

from playwright.sync_api import Page, expect


BASE_URL = os.getenv("BASE_URL", "https://app.workflowpro.com")

COMPANY1_EMAIL = os.getenv("COMPANY1_EMAIL", "admin@company1.com")
COMPANY1_PASSWORD = os.getenv("COMPANY1_PASSWORD", "password123")

COMPANY2_EMAIL = os.getenv("COMPANY2_EMAIL", "user@company2.com")
COMPANY2_PASSWORD = os.getenv("COMPANY2_PASSWORD", "password123")


def login(page: Page, email: str, password: str) -> None:
    """Log in and wait for the application to reach the dashboard."""

    page.goto(
        f"{BASE_URL}/login",
        wait_until="domcontentloaded",
    )

    page.locator("#email").fill(email)
    page.locator("#password").fill(password)
    page.locator("#login-btn").click()

    expect(page).to_have_url(
        f"{BASE_URL}/dashboard",
        timeout=15_000,
    )


def test_user_login(page: Page):
    """Verify that a valid user can successfully log in."""

    login(page, COMPANY1_EMAIL, COMPANY1_PASSWORD)

    expect(
        page.locator(".welcome-message")
    ).to_be_visible(timeout=15_000)


def test_multi_tenant_access(page: Page):
    """Verify Company 2 users only see Company 2 projects."""

    login(page, COMPANY2_EMAIL, COMPANY2_PASSWORD)

    project_cards = page.locator(".project-card")

    expect(
        project_cards.first
    ).to_be_visible(timeout=15_000)

    project_count = project_cards.count()

    assert project_count > 0, (
        "No projects were displayed for Company 2."
    )

    for index in range(project_count):
        project_text = (
            project_cards.nth(index).text_content() or ""
        )

        assert "Company2" in project_text, (
            f"Possible tenant-isolation issue: "
            f"project card {index} does not belong to Company2."
        )