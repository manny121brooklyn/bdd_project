import pytest
from selenium import webdriver


# Fixture
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    print('Browser opened')

    yield driver
    print('Browser closing ...')
    driver.quit()
