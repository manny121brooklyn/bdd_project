import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest_bdd
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page.HeaderPanel


# CONSTANTS
HOME_URL = "https://automationexercise.com/products"

# Scenarios
scenarios("../features/search_page.feature")
# Steps

@given("The store home page is displayed")
def test_start_homepage(browser):
    print('Home page starting ...')
    browser.get(HOME_URL)

@when(parsers.parse('The user searches for "{phrase}"'))
def test_search_web(browser, phrase):
    # element locators
    # print('Search is starting ...')
    search_box = browser.find_element(By.ID, "search_product")
    search_box.send_keys(phrase)
    time.sleep(2)
    search_button = browser.find_element(By. ID, "submit_search")
    search_button.click()
    time.sleep(2)
    # browser.execute_script('arguments[0].click()', search_box)

@then("At least one product is listed")
def test_verify_product_list(browser):
    # elements from the list
    products = browser.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
    assert len(products) >= 1
    print('search result verified')

