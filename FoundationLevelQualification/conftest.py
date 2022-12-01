import pytest
from selenium import webdriver
import os


@pytest.fixture(scope="class")
def init_driver(request):
    pass

    browser1 = 'chrome'

    browser = os.environ.get('BROWSER', browser1)
    if not browser:
        raise Exception("The environment variable 'BROWSER' is not set")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()

    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()
