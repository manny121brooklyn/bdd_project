from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class HeaderPanel():
    def __init__(self, browser):
        self.browser = browser

    # Locators

        self.search_box = browser.find_element(By.ID, "search_product")
        self.search_button = browser.find_element(By.ID, "submit_search")
        self.products = browser.find_elements(
            By.CSS_SELECTOR, ".product-image-wrapper .single-products")

    def get_product_count(self, products):
        return len(products)

    def click_search_button(self, search_button):
        search_button.click()