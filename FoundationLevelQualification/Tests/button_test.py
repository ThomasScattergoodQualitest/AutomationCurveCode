from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#
# def clear_box(locator, timeout=None):
#     default_timeout = 10
#     timeout = timeout if timeout else default_timeout
#
#     WebDriverWait(driver, timeout).until(
#         EC.visibility_of_element_located(locator)
#     ).send_keys(Keys.DELETE)
#
#
# driver = webdriver.Chrome()
# url = "https://www.clock-software.com/demo-clockpms/index.html"
# driver.get(url)
#
# ARRIVAL_BOX = driver.find_element(By.CSS_SELECTOR, '.form-control[name="wbe_product[arrival]"')
# ARRIVAL_BOX.send_keys("25-12-2022")
# time.sleep(1)
#
# NIGHTS_BOX = driver.find_element(By.ID, "to-place")
# NIGHTS_BOX.send_keys(Keys.DELETE)
# NIGHTS_BOX.send_keys(4)
# time.sleep(1)
#
# ADULTS_BOX = driver.find_element(By.CSS_SELECTOR, '.form-control[name="wbe_product[adult_count]"')
# ADULTS_BOX.send_keys(Keys.DELETE)
# ADULTS_BOX.send_keys(4)
# time.sleep(1)
#
# CHILDREN_BOX = driver.find_element(By.CSS_SELECTOR, '.form-control[name="wbe_product[children_count]"')
# CHILDREN_BOX.send_keys(Keys.DELETE)
# CHILDREN_BOX.send_keys(1)
# time.sleep(1)
#
# driver.find_element(By.XPATH, '//*[@id="flights"]/form/div/div[5]/input').click()
#
# time.sleep(2)
#
#
# def wait_and_get_element(locator, timeout=None, err=None, default_timeout=10):
#     timeout = timeout if timeout else default_timeout
#     err = err if err else f"unable to find element located by '{locator}'," \
#                           f"after timeout of {timeout}"
#     try:
#         element = WebDriverWait(driver, timeout).until(
#             EC.visibility_of_element_located(locator)
#         )
#     except TimeoutException:
#         raise TimeoutException(err)
#     print("number of elements: " + str(len(element)))
#
#
# ROOM_SELECT_BTN = driver.find_element(By.XPATH, '//*[@id="bookable_container_15343"]/div[2]/div[2]/table/tbody/tr/td['
#                                                 '3]/span/a')
#
#
# ROOM_SELECT_BUTTONS = driver.find_elements(By.CSS_SELECTOR, 'btn btn-success ')
# print("Number of buttons: " + str(len(ROOM_SELECT_BUTTONS)))
# print("TEST PASSED")
#
# # ROOM_SELECT_BTN.is_displayed()
# # ROOM_SELECT_BTN.get_attribute()
#
# wait_and_get_element(ROOM_SELECT_BTN)
#
# driver.quit()
