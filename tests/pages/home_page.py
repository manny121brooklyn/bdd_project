from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class HeaderPanel():
    def __init__(self, browser):
        self.browser = browser
        self.search_box = browser.find_element(By.ID, "search_product")
        self.search_button = browser.find_element(By.ID, "submit_search")
        self.products = browser.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")





