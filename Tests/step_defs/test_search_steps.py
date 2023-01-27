import time

from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.home_page import HeaderPanel
# when importing you might import parent of pages which is tests
# as above


# CONSTANTS
HOME_URL = "https://automationexercise.com/products"

# Scenarios
scenarios("../features/search_page.feature")


# Steps

@given("The store home page is displayed")
def test_start_homepage(browser):
    browser.get(HOME_URL)
    time.sleep(2)


@when(parsers.parse('The user searches for {phrase}'))
def test_search_web(browser, phrase):
    # element locators
    HeaderPanel.search_box.send_keys(phrase)
    time.sleep(2)
    HeaderPanel.click_search_button()
    time.sleep(2)
    # browser.execute_script('arguments[0].click()', search_box)


@then("At least one product is listed")
def test_verify_product_list(browser):
    assert HeaderPanel.get_product_count() >= 1
