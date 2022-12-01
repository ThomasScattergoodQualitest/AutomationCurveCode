from selenium.webdriver.common.by import By


class ExtraServicesPageLocators:
    AIRPORT_TRANSFER_BOX = (By.XPATH, "//*[contains(text(),'Airport')]/../following-sibling::div/input")
    AIRPORT_TRANSFER_PRICE = (By.XPATH, "//*[contains(text(),'Airport')]/../following-sibling::div/div")

    BUSINESS_SERVICES_BOX = (By.XPATH, "//*[contains(text(),'Business')]/../following-sibling::div/input")
    BUSINESS_SERVICES_PRICE = (By.XPATH, "//*[contains(text(),'Business')]/../following-sibling::div/div")

    DRY_CLEANING_BOX = (By.XPATH, "//*[contains(text(),'Cleaning')]/../following-sibling::div/input")
    DRY_CLEANING_PRICE = (By.XPATH, "//*[contains(text(),'Cleaning')]/../following-sibling::div/div")

    FITNESS_BOX = (By.XPATH, "//*[contains(text(),'Fitness')]/../following-sibling::div/input")
    FITNESS_PRICE = (By.XPATH, "//*[contains(text(),'Fitness')]/../following-sibling::div/div")

    ADD_SERVICES_BTN = (By.XPATH, "//form//span[@class='pull-right']//input")
    No_BTN = (By.XPATH, "//form//span[@class='pull-right']//a[contains(text(),'No, thanks. >>')]")
