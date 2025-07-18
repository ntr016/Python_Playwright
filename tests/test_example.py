from playwright.sync_api import expect
from .pages.home_page import Home_page


def test_home_page_navigation(page, base_url):
    home = Home_page(page)
    home.open(base_url)
    home.check_title()
    home.go_to_login()
    expect(page).to_have_url(f"{base_url}/login")
    

    
