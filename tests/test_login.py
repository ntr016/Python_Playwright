from .pages.login_page import LoginPage


def test_successful_login(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login("tomsmith", "SuperSecretPassword!")
    login.assert_login_success()
