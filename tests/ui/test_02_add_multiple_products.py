import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-02: Add multiple products to cart")
def test_add_multiple_products(page: Page):
    page.goto(f"{BASE_URL}/products")

    with allure.step("Add first product"):
        page.locator(".productinfo a.add-to-cart").nth(0).click()
        page.get_by_text("Continue Shopping", exact=True).click()

    with allure.step("Add second product"):
        page.locator(".productinfo a.add-to-cart").nth(1).click()
        page.get_by_text("View Cart", exact=True).click()

    with allure.step("Verify cart contains two products"):
        expect(page).to_have_url(f"{BASE_URL}/view_cart")
        expect(page.locator("#cart_info_table tbody tr")).to_have_count(2)
