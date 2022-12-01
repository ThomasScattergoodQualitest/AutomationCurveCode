from selenium.webdriver.common.by import By


class RoomPageLocators:
    ROOM_TYPE = (By.XPATH, '//h2[contains(text(),"Deluxe Appartment")]/../../following-sibling::div//tr//td//h4')

    ROOM_PRICE = (By.XPATH, "//h2[contains(text(),'Deluxe Appartment')]/../../following-sibling::div//td["
                            "@class='text-right hidden-xs']//h4[contains(text(), 'EUR')]")

    ROOM_SELECT_BTN = (By.XPATH, "//h2[contains(text(),'Deluxe Appartment')]/../../following-sibling::div//span["
                                 "@class='pull-right']//a[contains(text(),'Select')]")

    IFRAME = (By.ID, 'clock_pms_iframe_1')
