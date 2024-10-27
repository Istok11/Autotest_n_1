from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver

def test_open_s6(driver):
    driver.get('https://demoblaze.com/')
    galxy_s6 = driver.find_element(By.XPATH, value = '//a[text()="Samsung galaxy s6"]')
    galxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, value='H2')
    assert title.text == 'Samsung galaxy s6'
