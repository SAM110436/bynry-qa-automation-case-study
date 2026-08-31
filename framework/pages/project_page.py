from playwright.sync_api import Page, expect


class ProjectPage:
    """Page Object for project listing and project validation."""

    PROJECT_CARD = ".project-card"

    def __init__(self, page: Page):
        self.page = page

    def wait_for_projects(self) -> None:
        """Wait until at least one project is rendered."""

        expect(
            self.page.locator(self.PROJECT_CARD).first
        ).to_be_visible(timeout=15_000)

    def get_project_count(self) -> int:
        """Return the number of visible project cards."""

        return self.page.locator(self.PROJECT_CARD).count()

    def get_project_text(self, index: int) -> str:
        """Return project card text."""

        return (
            self.page.locator(self.PROJECT_CARD)
            .nth(index)
            .text_content()
            or ""
        )

    def verify_projects_belong_to_tenant(
        self,
        tenant_name: str,
    ) -> None:
        """Verify every displayed project belongs to the expected tenant."""

        self.wait_for_projects()

        project_count = self.get_project_count()

        assert project_count > 0, (
            f"No projects displayed for tenant {tenant_name}."
        )

        for index in range(project_count):
            project_text = self.get_project_text(index)

            assert tenant_name in project_text, (
                f"Tenant isolation issue: project {index} "
                f"does not belong to {tenant_name}."
            )