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
@allure.title("API-01: Get all products")
def test_get_all_products(api_context):
    with allure.step("Send GET request"):
        response = api_context.get(f"{BASE_URL}/productsList")

    with allure.step("Verify response status"):
        assert response.status == 200

    with allure.step("Verify products response"):
        data = response.json()

        assert data["responseCode"] == 200
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0
