from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from FoundationLevelQualification.src.Pages.Locators.ExtraServicesPageLocators import ExtraServicesPageLocators
from FoundationLevelQualification.src.SeleniumExtended import SeleniumExtended


class ExtraServicesPage(ExtraServicesPageLocators):
    def __init__(self, driver):
        self.default_timeout = 10
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def select_airport_transfer(self):
        self.sl.wait_and_input_text(self.AIRPORT_TRANSFER_BOX, 1)

    def select_business_services_box(self):
        self.sl.wait_and_input_text(self.BUSINESS_SERVICES_BOX, 1)

    def select_dry_cleaning(self):
        self.sl.wait_and_input_text(self.DRY_CLEANING_BOX, 1)

    def select_fitness(self):
        self.sl.wait_and_input_text(self.FITNESS_BOX, 1)

    def click_add_services_button(self):
        # self.sl.wait_and_click(self.ADD_SERVICES_BTN)
        element = self.sl.driver.find_element(By.XPATH, "//form//span[@class='pull-right']//input")
        self.driver.execute_script("arguments[0].click();", element)

    def click_no_button(self):
        self.sl.wait_and_click(self.No_BTN)

    def store_airport_price(self):
        airport_transfer_price = self.sl.wait_and_get_text(self.AIRPORT_TRANSFER_PRICE)
        price_split = airport_transfer_price.split()
        price = ' '.join(price_split[0:2])
        actual_price = 15
        print(f"Price of airport transfer is: {price}")

    def store_business_services_price(self):
        business_services_price = self.sl.wait_and_get_text(self.BUSINESS_SERVICES_PRICE)
        price_split = business_services_price.split()
        price = float(' '.join(price_split[3:4]))
        number_of_nights = self.sl.wait_and_get_text(self.BUSINESS_SERVICES_PRICE)
        number_of_nights_split = number_of_nights.split()
        nights = float(' '.join(number_of_nights_split[0:1]))
        print(f"number of nights: {nights}")
        actual_price = price * nights
        print(f"Price of business services for length of stay is: {actual_price} Euros")


    def store_dry_cleaning_price(self):
        dry_cleaning_price = self.sl.wait_and_get_text(self.DRY_CLEANING_PRICE)
        price_split = dry_cleaning_price.split()
        price = ' '.join(price_split[0:2])
        print(f"Price of dry cleaning is: {price}")

    def store_fitness_price(self):
        fitness_price = self.sl.wait_and_get_text(self.FITNESS_PRICE)
        price_split = fitness_price.split()
        price = ' '.join(price_split[0:2])
        print(f"Price of fitness is: {price}")
