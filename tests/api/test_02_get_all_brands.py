import pytest
import allure
from playwright.sync_api import Playwright

BASE_URL = "https://automationexercise.com/api"


@pytest.fixture
def api_context(playwright: Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


@pytest.mark.api
@allure.tag("API")
@allure.title("API-02: Get all brands")
def test_get_all_brands(api_context):
    with allure.step("Send GET request"):
        response = api_context.get(f"{BASE_URL}/brandsList")

    with allure.step("Verify response status"):
        assert response.status == 200

    with allure.step("Verify brands response"):
        data = response.json()

        assert data["responseCode"] == 200
        assert isinstance(data["brands"], list)
        assert len(data["brands"]) > 0
