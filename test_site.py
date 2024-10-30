import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(driver):
    
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    # driver.get('https://demoblaze.com/')  шаг заменен 
    # galxy_s6 = driver.find_element(By.XPATH, value = '//a[text()="Samsung galaxy s6"]') шаг заменен 
    # galxy_s6.click() шаг заменен 
    # title = driver.find_element(By.CSS_SELECTOR, value='H2') шаг заменен 
    # assert title.text == 'Samsung galaxy s6' шаг заменен 

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    # driver.get('https://demoblaze.com/') шаг заменен 
    homepage.click_monitor()
    # monitor_link = driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''') шаг заменен 
    # monitor_link.click() шаг заменен 
    time.sleep(2)
    homepage.check_that_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR, value='.card') шаг заменен 
    # assert len(monitors) == 2 шаг заменен 