from selenium.webdriver.common.by import By


class HomePageLocators:

    ARRIVAL_BOX = (By.CSS_SELECTOR, '.form-control[name="wbe_product[arrival]"')
    NIGHTS_BOX = (By.ID, "to-place")
    ADULTS_BOX = (By.CSS_SELECTOR, '.form-control[name="wbe_product[adult_count]"')
    CHILDREN_BOX = (By.CSS_SELECTOR, '.form-control[name="wbe_product[children_count]"')
    BOOK_NOW_BTN = (By.XPATH, '//*[@id="flights"]/form/div/div[5]/input')
    TEST_TEXT = (By.CSS_SELECTOR, '#flights > form > div > div:nth-child(1) > div > label')
