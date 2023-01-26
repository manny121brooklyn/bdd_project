import pytest
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By


# CONSTANTS
HOME_URL = "https://automationexercise.com/products"

# Fixture
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield
    driver.quit()

# Steps
def test_start_homepage():
    browser.get(HOME_URL)

def test_search_web():
    # element locators
    search_box = browser.find_element(By.ID, "search_product")
    search_box = browser.find_element(By. ID, "submit_search")
    search_box.send_keys("dress")
    search_box.click()
    # browser.execute_script('arguments[0].click()', search_box)


