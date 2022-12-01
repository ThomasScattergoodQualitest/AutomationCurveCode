from selenium.webdriver.common.by import By


class CardDetailsPageLocators:
    CARD_NUMBER_BOX = (By.XPATH, '//*[contains(text(),"Number")]/..//input')
    CARD_BRAND_DROPDOWN = (By.XPATH, '//div[@class="form-group"]//div//select[@id="credit_card_collect_purchase_brand"]')
    CARD_EXPIRES_MONTH_DROPDOWN = (By.XPATH, '//div[@class="form-group"]//div//select[@id="cardExpirationMonth"]')
    CARD_EXPIRES_YEAR_DROPDOWN = (By.XPATH, '//div[@class="form-group"]//div//select[@id="cardExpirationYear"]')

    CARD_BILLING_ADDRESS_BOX = (By.XPATH, '//*[contains(text(),"Billing address")]/..//input')
    CARD_ZIP_BOX = (By.XPATH, '//*[contains(text(),"Zip")]/..//input')
    CARD_CITY_BOX = (By.XPATH, '//*[contains(text(),"City")]/..//input')
    CARD_STATE_BOX = (By.XPATH, '//*[contains(text(),"State")]/..//input')
    CARD_COUNTRY_DROPDOWN = (By.XPATH, '//div[@class="form-group"]//div//select['
                                       '@id="credit_card_collect_purchase_country"]')

    PAY_BUTTON = (By.XPATH, '//div[@class="form-group"]//div//button')

    SUCCESS_MSG_1 = (By.XPATH, '//div[@class="row"]//div[@id="common_alert"]/../h1')
    BOOKING_NUMBER = (By.XPATH, '//div[@class="row"]//div[@id="common_alert"]/../h3/span/span')
