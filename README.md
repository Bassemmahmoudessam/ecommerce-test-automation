
# Automation Exercise - Test Automation Project

## Project Overview
Automated testing project for https://automationexercise.com/
using Playwright, Python, Pytest, and Allure Report.

## Tools & Technologies
- Python
- Playwright
- Pytest
- Allure Report
- API Testing

## Test Coverage
### UI Testing
- Product Search
- Add Multiple Products to Cart
- Product Category Navigation
- Product Details Validation
- Contact Us Form
- Responsive Layout
- Cart Persistence

### API Testing
- Get All Products
- Get All Brands
- Search Products

## Installation
1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Install Playwright browser:

   playwright install chromium

4. Run all tests:

npx allure-commandline serve allure-results

## Allure Report
Generate and open the report:

   allure serve allure-results

## Project Structure
- tests/ui/ - UI automation tests
- tests/api/ - API automation tests
- conftest.py - Shared test fixtures
- pytest.ini - Pytest configuration
- requirements.txt - Project dependencies

## Author
Bassem Mahmoud Essam
