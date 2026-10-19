import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-04: Verify product details")
def test_product_details(page: Page):
    page.goto(f"{BASE_URL}/products")

    with allure.step("Open first product details"):
        page.get_by_text("View Product", exact=True).first.click()

    with allure.step("Verify product information"):
        expect(page.locator(".product-information")).to_be_visible()
        expect(page.locator(".product-information h2")).to_be_visible()
        expect(page.get_by_text("Availability:", exact=False)).to_be_visible()
        expect(page.get_by_text("Condition:", exact=False)).to_be_visible()
        expect(page.get_by_text("Brand:", exact=False)).to_be_visible()
        expect(page.locator("input#quantity")).to_be_visible()
        expect(page.get_by_role("button", name="Add to cart")).to_be_visible()
