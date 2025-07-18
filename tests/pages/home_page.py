from playwright.sync_api import Page, expect
from .base_page import BasePage


class Home_page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.expected_title = "The Internet"

    def open(self, base_url: str):
        self.goto(base_url)

    def check_title(self):
        expect(self.page).to_have_title(self.expected_title)

    def go_to_login(self):
        self.page.click("text=Form Authentication")


