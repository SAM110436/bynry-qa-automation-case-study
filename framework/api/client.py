import os
from typing import Any

import requests


class APIClient:
    """Simple API client for WorkFlow Pro services."""

    def __init__(
        self,
        base_url: str | None = None,
        token: str | None = None,
        tenant_id: str | None = None,
    ):
        self.base_url = (
            base_url
            or os.getenv(
                "API_BASE_URL",
                "https://app.workflowpro.com/api/v1",
            )
        ).rstrip("/")

        self.token = token or os.getenv("API_TOKEN", "")
        self.tenant_id = tenant_id or os.getenv(
            "TENANT_ID",
            "company1",
        )

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id,
            "Content-Type": "application/json",
        }

    def create_project(
        self,
        name: str,
        description: str,
        team_members: list[str],
    ) -> dict[str, Any]:
        """Create a project through the API."""

        response = requests.post(
            f"{self.base_url}/projects",
            headers=self._headers(),
            json={
                "name": name,
                "description": description,
                "team_members": team_members,
            },
            timeout=15,
        )

        response.raise_for_status()
        return response.json()

    def get_projects(self) -> list[dict[str, Any]]:
        """Retrieve projects for the configured tenant."""

        response = requests.get(
            f"{self.base_url}/projects",
            headers=self._headers(),
            timeout=15,
        )

        response.raise_for_status()
        return response.json()