import pytest
import allure
from playwright.sync_api import Page, expect

BASE_URL = "https://automationexercise.com"


@pytest.mark.ui
@allure.tag("UI")
@allure.title("UI-06: Check responsive layout")
def test_responsive_layout(page: Page):
    with allure.step("Open homepage in mobile viewport"):
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(BASE_URL)

    with allure.step("Verify page is visible"):
        expect(page.locator("body")).to_be_visible()

    with allure.step("Check horizontal overflow"):
        has_overflow = page.evaluate(
            "() => document.documentElement.scrollWidth " "> window.innerWidth"
        )
        assert not has_overflow, "Page has horizontal overflow on mobile"
