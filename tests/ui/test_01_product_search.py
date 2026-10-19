import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-01: Search products")
def test_product_search(page: Page):
    with allure.step("Open Products page"):
        page.goto(f"{BASE_URL}/products")
        expect(page.get_by_text("All Products", exact=True)).to_be_visible()

    with allure.step("Search for dress"):
        page.locator("#search_product").fill("dress")
        page.locator("#submit_search").click()

    with allure.step("Verify search results"):
        expect(page.get_by_text("Searched Products", exact=True)).to_be_visible()
        expect(
            page.locator(".features_items .product-image-wrapper").first
        ).to_be_visible()
