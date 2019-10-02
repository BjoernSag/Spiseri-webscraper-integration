from selenium import webdriver
import pytest

#Test opening of window and maximizing
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='/Users//yumo0/OneDrive/sanitySites/recipe-pyth-api/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test complete")

def test_images(test_setup):
    driver.get("https://www.rema.no/kampanjevarer/")
    images = driver.find_elements_by_tag_name('img')

def test_input(test_setup):
    driver.get("https://www.rema.no/kampanjevarer/")
    driver.find_element_by_id('kundeavis.search').send_keys('stavanger')
    driver.implicitly_wait(10)
