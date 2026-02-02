from playwright.sync_api import Page
import pytest
import time

## @pytest.mark.skip_browser("edge")
def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"
    time.sleep(2)
    
def test_invetory_size(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    #assert page.title() == "Swab Labs"
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    time.sleep(2)