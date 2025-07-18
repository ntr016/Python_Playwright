from .pages.home_page import Home_page
import time

def test_example(page, base_url):
    home = Home_page(page)
    home.goto(base_url)
    home.check_title()
    page.click("text=Get Started")
    page.click("text=Introduction")    
    

    
