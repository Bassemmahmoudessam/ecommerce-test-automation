import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-07: Verify cart after page navigation")
def test_cart_persistence_during_navigation(page: Page):
    page.goto(f"{BASE_URL}/products")

    with allure.step("Add a product to cart"):
        page.locator(".productinfo a.add-to-cart").first.click()
        page.get_by_text("View Cart", exact=True).click()

    with allure.step("Verify product is in cart"):
        expect(page.locator("#cart_info_table tbody tr")).to_have_count(1)

    with allure.step("Navigate away and return to cart"):
        page.goto(BASE_URL)
        page.goto(f"{BASE_URL}/view_cart")

    with allure.step("Verify product remains in cart"):
        expect(page.locator("#cart_info_table tbody tr")).to_have_count(1)
