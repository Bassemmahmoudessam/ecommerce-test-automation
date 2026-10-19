import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-05: Submit Contact Us form")
def test_contact_us_form(page: Page):
    page.goto(f"{BASE_URL}/contact_us")

    with allure.step("Fill contact form"):
        page.locator('[data-qa="name"]').fill("Test User")
        page.locator('[data-qa="email"]').fill("test.user@example.com")
        page.locator('[data-qa="subject"]').fill("Automation Test")
        page.locator('[data-qa="message"]').fill(
            "This is an automated contact form test."
        )

    with allure.step("Handle confirmation dialog"):
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator('[data-qa="submit-button"]').click()

    with allure.step("Verify successful submission"):
        expect(
            page.get_by_text(
                "Success! Your details have been submitted successfully.",
                exact=True,
            )
        ).to_be_visible()
