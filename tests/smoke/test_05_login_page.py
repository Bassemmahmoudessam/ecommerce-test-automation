import allure

from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com/"


@allure.tag("SMOKE")
def test_05_login_page_visibility(page: Page):
    """Verify login error and signup transition."""
    page.goto(BASE_URL)
    page.locator("a[href='/login']").click()

    expect(page.locator("h2:text('Login to your account')")).to_be_visible()
    expect(page.locator("h2:text('New User Signup!')")).to_be_visible()

    page.fill("input[data-qa='login-email']", "invalid_email@test.com")
    page.fill("input[data-qa='login-password']", "WrongPassword123")
    page.click("button[data-qa='login-button']")

    login_error = page.locator("form[action*='login'] p")

    expect(login_error).to_be_visible()
    expect(login_error).to_contain_text("Your email or password is incorrect!")

    page.fill("input[data-qa='signup-name']", "NewTester")
    page.fill("input[data-qa='signup-email']", "newtester_999@test.com")
    page.click("button[data-qa='signup-button']")

    expect(page.locator("b:text('Enter Account Information')")).to_be_visible()
    expect(page.locator("#id_gender1")).to_be_visible()
    expect(page.locator("input[data-qa='password']")).to_be_visible()
