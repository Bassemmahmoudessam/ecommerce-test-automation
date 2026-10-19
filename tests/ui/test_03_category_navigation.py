import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-03: Navigate through product categories")
def test_category_navigation(page: Page):
    page.goto(BASE_URL)

    with allure.step("Open Women category"):
        page.get_by_text("Women", exact=True).click()
        page.get_by_role("link", name="Dress", exact=True).click()

    with allure.step("Verify category page"):
        expect(page).to_have_url(f"{BASE_URL}/category_products/1")
        expect(page.get_by_text("Women - Dress Products", exact=True)).to_be_visible()
