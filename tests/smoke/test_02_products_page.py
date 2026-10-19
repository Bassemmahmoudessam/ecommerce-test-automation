import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com/"


@allure.tag("SMOKE")
def test_02_products_page_navigation(page: Page):
    """Navigate products, category, and product details."""
    page.goto(BASE_URL)
    page.locator("a[href='/products']").click()

    expect(page).to_have_url(f"{BASE_URL}products")
    expect(page.locator(".features_items")).to_be_visible()

    expect(page.locator("div.left-sidebar")).to_be_visible()
    expect(page.locator("h2:has-text('Category')")).to_be_visible()
    expect(page.locator("h2:has-text('Brands')")).to_be_visible()

    page.locator("a[href='#Women']").click()
    page.locator("a[href='/category_products/1']").click()

    expect(page.locator(".title.text-center")).to_contain_text("Women - Dress Products")

    page.locator("a[href*='/product_details/']").first.click()

    expect(page.locator("div.product-information")).to_be_visible()
    expect(page.locator(".product-information h2")).to_be_visible()
    expect(page.locator(".product-information span:has-text('Rs.')")).to_be_visible()
