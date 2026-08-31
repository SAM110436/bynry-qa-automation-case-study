import json
import os
import urllib.parse


def get_browserstack_ws_endpoint(
    device: str,
    os_name: str,
    os_version: str,
) -> str:
    """
    Build the BrowserStack Playwright WebSocket endpoint.

    Credentials are read from environment variables and are
    intentionally never stored in source control.
    """

    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if not username or not access_key:
        raise RuntimeError(
            "BROWSERSTACK_USERNAME and "
            "BROWSERSTACK_ACCESS_KEY must be configured."
        )

    capabilities = {
        "browser": "chrome",
        "browser_version": "latest",
        "os": os_name,
        "os_version": os_version,
        "device": device,
        "browserstack.username": username,
        "browserstack.accessKey": access_key,
        "projectName": "Bynry QA Automation Case Study",
        "buildName": "Bynry QA Automation",
        "name": f"Mobile - {device}",
        "browserstack.debug": "true",
        "browserstack.networkLogs": "true",
    }

    encoded_caps = urllib.parse.quote(
        json.dumps(capabilities)
    )

    return (
        "wss://cdp.browserstack.com/playwright"
        f"?caps={encoded_caps}"
    )