import os


BROWSERSTACK_USERNAME = os.getenv(
    "BROWSERSTACK_USERNAME",
    "",
)

BROWSERSTACK_ACCESS_KEY = os.getenv(
    "BROWSERSTACK_ACCESS_KEY",
    "",
)


def get_browserstack_capabilities(
    device: str,
    os_name: str,
    os_version: str,
) -> dict:
    """Build BrowserStack capabilities for mobile testing."""

    return {
        "browserName": "chrome",
        "bstack:options": {
            "deviceName": device,
            "os": os_name,
            "osVersion": os_version,
            "userName": BROWSERSTACK_USERNAME,
            "accessKey": BROWSERSTACK_ACCESS_KEY,
            "projectName": "Bynry QA Automation Case Study",
            "buildName": "QA Automation Build",
            "sessionName": f"Mobile Test - {device}",
        },
    }