import allure

from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com/"


@allure.tag("SMOKE")
def test_03_product_search(page: Page):
    """Search for a product and add it to the cart."""
    page.goto(f"{BASE_URL}products")
    page.fill("#search_product", "Top")
    page.click("#submit_search")

    expect(page.locator(".features_items")).to_be_visible()
    expect(page.locator(".title.text-center")).to_contain_text("Searched Products")
    expect(page.locator(".product-image-wrapper").first).to_be_visible()

    product_card = page.locator(".product-image-wrapper").first
    product_card.hover()

    expect(product_card.locator(".add-to-cart").first).to_be_visible()

    product_card.locator(".add-to-cart").first.click()

    expect(page.locator("#cartModal")).to_be_visible()
    expect(page.locator("h4.modal-title:has-text('Added!')")).to_be_visible()

    page.locator("button.close-modal").click()
