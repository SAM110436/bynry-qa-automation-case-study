import os
import uuid

import pytest
from playwright.sync_api import Page, expect

from framework.api.client import APIClient
from framework.pages.login_page import LoginPage
from framework.pages.project_page import ProjectPage
from framework.settings import settings


def test_project_creation_flow(page: Page):
    """
    End-to-end integration flow:

    1. Create project through API.
    2. Log in through web UI.
    3. Verify project appears for the correct tenant.
    4. Verify another tenant cannot see the project.

    Mobile validation is handled separately because BrowserStack
    requires its own remote browser/device configuration.
    """

    # ---------------------------------------------------------
    # 1. Test data
    # ---------------------------------------------------------

    unique_name = f"QA Automation Project {uuid.uuid4().hex[:8]}"

    description = "Project created by Bynry QA automation case study."

    team_members = [
        settings.COMPANY1_EMAIL,
    ]

    # ---------------------------------------------------------
    # 2. API: Create project for Company 1
    # ---------------------------------------------------------

    api_client = APIClient(
        token=os.getenv("API_TOKEN", "test-token"),
        tenant_id="company1",
    )

    try:
        project = api_client.create_project(
            name=unique_name,
            description=description,
            team_members=team_members,
        )
    except Exception as exc:
        pytest.fail(f"Project creation API request failed: {exc}")

    assert project["name"] == unique_name
    assert project["status"] == "active"

    project_id = project["id"]

    # ---------------------------------------------------------
    # 3. UI: Login as Company 1
    # ---------------------------------------------------------

    login_page = LoginPage(page)

    login_page.open(settings.BASE_URL)

    login_page.login(
        settings.COMPANY1_EMAIL,
        settings.COMPANY1_PASSWORD,
    )

    login_page.verify_dashboard(settings.BASE_URL)

    # ---------------------------------------------------------
    # 4. UI: Verify project belongs to Company 1
    # ---------------------------------------------------------

    project_page = ProjectPage(page)

    project_page.wait_for_projects()

    matching_project = page.locator(
        ".project-card",
        has_text=unique_name,
    )

    expect(matching_project).to_be_visible(
        timeout=15_000,
    )

    assert unique_name in (
        matching_project.text_content() or ""
    )

    # ---------------------------------------------------------
    # 5. Tenant isolation
    #
    # Log in as Company 2 and verify that the project created
    # for Company 1 is not visible.
    # ---------------------------------------------------------

    page.context.clear_cookies()

    login_page.open(settings.BASE_URL)

    login_page.login(
        settings.COMPANY2_EMAIL,
        settings.COMPANY2_PASSWORD,
    )

    login_page.verify_dashboard(settings.BASE_URL)

    company2_project = page.locator(
        ".project-card",
        has_text=unique_name,
    )

    expect(company2_project).to_have_count(
        0,
        timeout=15_000,
    )

    # The project ID is retained because a production framework
    # could use it for API cleanup after the test.
    assert project_id is not None