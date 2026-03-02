from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest

@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

def test_search(driver):
    driver.get('https://dtf.ru/games')
    sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, 'button.quick-search-button')
    search_button.click()
    sleep(5)
    search_field = driver.find_element(By.CSS_SELECTOR, 'input.text-input')
    search_field.send_keys('fallout')
    search_field.send_keys(Keys.ENTER)
    sleep(5)
    assert 'q=fallout' in driver.current_url