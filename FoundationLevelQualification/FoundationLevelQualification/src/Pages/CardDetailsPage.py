from selenium.webdriver.common.by import By

from FoundationLevelQualification.src.Pages.Locators.CardDetailsPageLocators import CardDetailsPageLocators
from FoundationLevelQualification.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.support.ui import Select


class CardDetailsPage(CardDetailsPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_card_number(self):
        card_number = 4444333322221111
        self.sl.wait_and_input_text(self.CARD_NUMBER_BOX, card_number)

    def input_card_brand(self):
        dropdown = self.driver.find_element(By.XPATH, '//div[@class="form-group"]//div//select['
                                                      '@id="credit_card_collect_purchase_brand"]')
        brand = Select(dropdown)
        brand.select_by_visible_text("VISA")

    def input_card_expiry_date(self):
        dropdown_month = self.driver.find_element(By.XPATH, '//div[@class="form-group"]//div//select['
                                                            '@id="cardExpirationMonth"]')
        month = Select(dropdown_month)
        month.select_by_visible_text("04")

        dropdown_year = self.driver.find_element(By.XPATH, '//div[@class="form-group"]//div//select['
                                                           '@id="cardExpirationYear"]')
        year = Select(dropdown_year)
        year.select_by_visible_text("2023")

    def input_billing_address(self):
        self.sl.wait_and_input_text(self.CARD_BILLING_ADDRESS_BOX, "123 Test Street")

    def input_zip_code(self):
        self.sl.wait_and_input_text(self.CARD_ZIP_BOX, "Test Zip")

    def input_city(self):
        self.sl.wait_and_input_text(self.CARD_CITY_BOX, "Test city")

    def input_state(self):
        self.sl.wait_and_input_text(self.CARD_STATE_BOX, "Test state")

    def input_country(self):
        dropdown_country = self.driver.find_element(By.XPATH, '//div[@class="form-group"]//div//select['
                                                              '@id="credit_card_collect_purchase_country"]')
        country = Select(dropdown_country)
        country.select_by_visible_text("United Kingdom")

    def click_pay_button(self):
        self.sl.wait_and_click(self.PAY_BUTTON)

    def validate_success_message(self):
        message = self.sl.wait_and_get_text(self.SUCCESS_MSG_1)
        assert message == 'Thank you for your booking!', f"Unexpected Thank you message"

        number = self.sl.wait_and_get_text(self.BOOKING_NUMBER)
        print(f"Your booking number is: {number}")
