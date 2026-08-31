from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the WorkFlow Pro login page."""

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-btn"
    WELCOME_MESSAGE = ".welcome-message"

    def __init__(self, page: Page):
        self.page = page

    def open(self, base_url: str) -> None:
        self.page.goto(
            f"{base_url}/login",
            wait_until="domcontentloaded",
        )

    def login(self, email: str, password: str) -> None:
        self.page.locator(self.EMAIL_INPUT).fill(email)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def verify_dashboard(self, base_url: str) -> None:
        expect(self.page).to_have_url(
            f"{base_url}/dashboard",
            timeout=15_000,
        )

        expect(
            self.page.locator(self.WELCOME_MESSAGE)
        ).to_be_visible(timeout=15_000)