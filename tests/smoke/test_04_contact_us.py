import allure

from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com/"


@allure.tag("SMOKE")
def test_04_contact_us_form_visibility(page: Page):
    """Submit the Contact Us form and verify success."""
    page.goto(BASE_URL)
    page.locator("a[href='/contact_us']").click()

    expect(
        page.locator("h2.title.text-center:has-text('Get In Touch')")
    ).to_be_visible()

    page.fill("input[data-qa='name']", "Smoke Test User")
    page.fill("input[data-qa='email']", "smoke_user@test.com")
    page.fill("input[data-qa='subject']", "Automated Smoke Inquiry")
    page.fill("textarea[data-qa='message']", "Testing contact us submission form flow.")

    page.once("dialog", lambda dialog: dialog.accept())
    page.click("input[data-qa='submit-button']")

    success_message = page.locator(".status.alert.alert-success")

    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text(
        "Success! Your details have been submitted successfully."
    )
