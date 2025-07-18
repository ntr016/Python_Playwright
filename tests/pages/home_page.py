from playwright.sync_api import Page, expect

class Home_page:
    def __init__(self, page: Page):
        self.page =page

    def goto(self, base_url):
        self.page.goto(base_url)

    def check_title(self):
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
        print(self.page.title())
    
    def click_elem(self, element):
        element.click()


