from FoundationLevelQualification.src.Pages.Locators.RoomPageLocators import RoomPageLocators
from FoundationLevelQualification.src.SeleniumExtended import SeleniumExtended


class RoomPage(RoomPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def store_room_type(self):
        room_type = self.sl.wait_and_get_text(self.ROOM_TYPE)
        print("")
        print(f"Room type is {room_type}")

    def store_room_price(self):
        room_price = self.sl.wait_and_get_text(self.ROOM_PRICE)
        print(f"Price of room is {room_price}")

    def click_select_room_button(self):
        self.sl.wait_until_element_is_clickable(self.ROOM_SELECT_BTN)

    # def select_button_elements(self):
    #     self.sl.wait_and_get_elements(self.ROOM_SELECT_BTNS)

    def switch_to_iframe(self):
        self.driver.switch_to.frame('clock_pms_iframe_1')

    def check_deluxe_room_availability(self):
        pass

    def click_check_availability_calender(self):
        pass

    def check_for_number_of_consecutive_nights(self):
        pass

    def click_next_dates_button(self):
        pass

    def select_date(self):
        pass

    def click_search_for_available_rooms_button(self):
        pass