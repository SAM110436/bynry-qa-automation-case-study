from playwright.sync_api import Browser, BrowserType


def pytest_playwright_browser_type_launch_args(browser_type: BrowserType):
    return {
        "args": ["--ignore-certificate-errors"],
    }