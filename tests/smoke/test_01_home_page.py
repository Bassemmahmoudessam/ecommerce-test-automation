import re
import allure

from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com/"


@allure.tag("SMOKE")
def test_01_home_page_load(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Automation Exercise")

    expect(page.locator("div").nth(3)).to_be_visible()
    expect(page.get_by_text("Category Women Dress Tops")).to_be_visible()

    expect(page.get_by_role("link", name=" Home")).to_be_visible()
    expect(page.get_by_role("link", name=" Products")).to_be_visible()
    expect(page.get_by_role("link", name=" Cart")).to_be_visible()
    expect(page.get_by_role("link", name=" Signup / Login")).to_be_visible()
    expect(page.get_by_role("link", name=" Contact us")).to_be_visible()

    page.get_by_role("link", name=" Test Cases").click()
    expect(page).to_have_url(f"{BASE_URL}test_cases")
    expect(page.locator("b")).to_be_visible()

    page.go_back()
    expect(page.locator("#footer")).to_be_visible()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
