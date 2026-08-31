import os


class Settings:
    """Central configuration for the QA automation framework."""

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://app.workflowpro.com",
    )

    API_BASE_URL = os.getenv(
        "API_BASE_URL",
        f"{BASE_URL}/api/v1",
    )

    TENANT_ID = os.getenv(
        "TENANT_ID",
        "company1",
    )

    BROWSER = os.getenv(
        "BROWSER",
        "chromium",
    )

    HEADLESS = os.getenv(
        "HEADLESS",
        "true",
    ).lower() == "true"

    COMPANY1_EMAIL = os.getenv(
        "COMPANY1_EMAIL",
        "admin@company1.com",
    )

    COMPANY1_PASSWORD = os.getenv(
        "COMPANY1_PASSWORD",
        "password123",
    )

    COMPANY2_EMAIL = os.getenv(
        "COMPANY2_EMAIL",
        "user@company2.com",
    )

    COMPANY2_PASSWORD = os.getenv(
        "COMPANY2_PASSWORD",
        "password123",
    )


settings = Settings()