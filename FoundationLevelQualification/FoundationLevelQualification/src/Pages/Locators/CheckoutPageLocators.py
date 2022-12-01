from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    EMAIL_BOX = (By.ID, 'booking_guest_attributes_e_mail')
    LAST_NAME_BOX = (By.ID, 'booking_guest_attributes_last_name')
    FIRST_NAME_BOX = (By.ID, 'booking_guest_attributes_first_name')
    PHONE_BOX = (By.ID, 'booking_guest_attributes_phone_number')
    IFRAME = (By.ID, 'clock_pms_iframe_1')

    CREDIT_CARD_RADIO_BTN = (By.ID, 'booking_payment_service_credit_card_collect')
    HOTEL_POLICY_BTN = (By.ID, 'booking_agreed')
    CREATE_BOOKING_BTN = (By.XPATH, '//div[@class="form-actions col-sm-8 col-sm-offset-4"]//input[@value="Create '
                                    'Booking"]')

    ARRIVAL_DATE = (By.XPATH, '//*[contains(text(),"Arrival")]/../following-sibling::div')
    NIGHTS_STAY = (By.XPATH, '//*[contains(text(),"Stay")]/../following-sibling::div')
    LEAVE_DATE = (By.XPATH, '//*[contains(text(),"Departure")]/../following-sibling::div')
    ROOM_TYPE = (By.XPATH, '//*[contains(text(),"Room Type")]/../following-sibling::div')
    ROOM_RATE = (By.XPATH, '//*[contains(text(),"Rate")]/../following-sibling::div')

    ROOMS_PRICE = (By.XPATH, '//*[contains(text(),"Rooms")]/../following-sibling::div')
    EXTRA_SERVICES_PRICE = (By.XPATH, '//*[contains(text(),"Extra Services")]/../following-sibling::div')
    VAT_PRICE = (By.XPATH, '//*[contains(text(),"VAT")]/../following-sibling::div')
    TOTAL_PRICE = (By.XPATH, '//*[contains(text(),"Total")]/../following-sibling::div')
