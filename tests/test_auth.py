"""import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"password\"]").click()

    # ---------------------
    context.close()
    browser.close()"""


import pytest
from pages.main_page import Main


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()