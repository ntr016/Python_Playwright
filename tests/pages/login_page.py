from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type=submit]")
        self.flash_message = page.locator("#flash")

    def open(self, base_url: str):
        self.goto(f"{base_url}/login")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_success(self):
        expect(self.flash_message).to_contain_text("You logged into a secure area!")
