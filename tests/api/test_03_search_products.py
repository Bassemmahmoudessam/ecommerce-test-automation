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
@allure.title("API-03: Search products")
def test_search_products(api_context):
    with allure.step("Send POST request with search parameter"):
        response = api_context.post(
            f"{BASE_URL}/searchProduct",
            form={"search_product": "top"},
        )

    with allure.step("Verify response status"):
        assert response.status == 200

    with allure.step("Verify search results"):
        data = response.json()

        assert data["responseCode"] == 200
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0

        for product in data["products"]:
            assert "name" in product
            assert "price" in product
            assert "id" in product
