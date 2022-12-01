from FoundationLevelQualification.src.Pages.Locators.CheckoutPageLocators import CheckoutPageLocators
from FoundationLevelQualification.src.SeleniumExtended import SeleniumExtended
from FoundationLevelQualification.src.Pages.HomePage import HomePage
import datetime


class CheckoutPage(CheckoutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_email(self):
        self.sl.wait_and_input_text(self.EMAIL_BOX, "JohnDoe@TestEmail.com")

    def input_last_name(self):
        self.sl.wait_and_input_text(self.LAST_NAME_BOX, "Doe")

    def input_first_name(self):
        self.sl.wait_and_input_text(self.FIRST_NAME_BOX, "John")

    def input_phone(self):
        self.sl.wait_and_input_text(self.PHONE_BOX, "12345678901")

    def verify_arrival_date(self):
        date = self.sl.wait_and_get_text(self.ARRIVAL_DATE)
        # homepage = HomePage(self.driver)
        assert date == (datetime.datetime.strptime(HomePage.future_string, "%d-%m-%Y")).strftime(
            '%d %b %Y'), "arrival date is not correct"
        print(f"Date of arrival is: {date}")

    def verify_number_of_nights(self):
        stay = self.sl.wait_and_get_text(self.NIGHTS_STAY)
        assert stay == str(4), 'Number of days stay is not equal to 4'
        print(f"Length of stay is: {stay} days")

    def verify_leaving_date(self):
        leave = self.sl.wait_and_get_text(self.LEAVE_DATE)
        print(f"Date of departure is: {leave}")

    def verify_room_type(self):
        room_type = self.sl.wait_and_get_text(self.ROOM_TYPE)
        print(f"The type of room is: {room_type}")

    def verify_room_rate(self):
        rate = self.sl.wait_and_get_text(self.ROOM_RATE)
        print(f"Rate of room is: {rate}")

    def verify_addons(self):
        addons = self.sl.wait_and_get_text(self.EXTRA_SERVICES_PRICE)
        print(f"Price of addons is: {addons}")

    def verify_room_cost(self):
        room_cost = self.sl.wait_and_get_text(self.ROOMS_PRICE)
        print(f"Cost of the room (including VAT) is: {room_cost}")

    def verify_total_cost(self):
        total = self.sl.wait_and_get_text(self.TOTAL_PRICE)
        print(f"Total cost of room, services and VAT is {total}")

    def select_credit_card(self):
        self.sl.wait_and_click(self.CREDIT_CARD_RADIO_BTN)

    def click_agree_with_hotel_policy(self):
        self.sl.wait_and_click(self.HOTEL_POLICY_BTN)

    def click_create_booking_button(self):
        self.sl.wait_and_click(self.CREATE_BOOKING_BTN)
