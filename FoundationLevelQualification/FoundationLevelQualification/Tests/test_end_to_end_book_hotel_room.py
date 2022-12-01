import pytest
from FoundationLevelQualification.src.Pages.HomePage import HomePage
from FoundationLevelQualification.src.Pages.RoomPage import RoomPage
from FoundationLevelQualification.src.Pages.ExtraServicesPage import ExtraServicesPage
from FoundationLevelQualification.src.Pages.CheckoutPage import CheckoutPage
from FoundationLevelQualification.src.Pages.CardDetailsPage import CardDetailsPage
import time


@pytest.mark.usefixtures("init_driver")
class TestEndToEndBookHotelRoom:

    @pytest.mark.tcid1
    def test_end_to_end_book_hotel_room(self):
        home_p = HomePage(self.driver)
        room_p = RoomPage(self.driver)
        ExtraS_p = ExtraServicesPage(self.driver)
        Checkout_p = CheckoutPage(self.driver)
        Card_p = CardDetailsPage(self.driver)
        # go to home page
        home_p.go_to_home_page()

        # input arrival date
        home_p.input_arrival_date()
        time.sleep(1)

        # input number of nights
        home_p.input_number_of_nights()

        # input number of adults and children
        home_p.input_number_of_adults()
        home_p.input_number_of_children()

        # click book now
        # time.sleep(3)
        home_p.click_book_now()

        # Test case passes up to this point

        #  select room
        room_p.switch_to_iframe()
        room_p.store_room_type()
        room_p.store_room_price()
        room_p.click_select_room_button()

        # select 2 extra services (send keys for quantity and click "add selected services")
        # ExtraS_p.select_airport_transfer()
        # ExtraS_p.store_airport_price()

        ExtraS_p.select_business_services_box()
        ExtraS_p.store_business_services_price()
        
        # ExtraS_p.select_dry_cleaning()
        # ExtraS_p.store_dry_cleaning_price()

        ExtraS_p.select_fitness()
        ExtraS_p.store_fitness_price()

        ExtraS_p.click_add_services_button()
        # ExtraS_p.click_no_button()

        # validate date, # of nights, room type, rate, add-ons and total
        # Checkout_p.verify_date()
        Checkout_p.verify_arrival_date()
        Checkout_p.verify_number_of_nights()
        Checkout_p.verify_leaving_date()
        Checkout_p.verify_room_type()
        Checkout_p.verify_room_rate()
        Checkout_p.verify_addons()
        Checkout_p.verify_room_cost()
        Checkout_p.verify_total_cost()

        # input contact info
        Checkout_p.input_email()
        Checkout_p.input_last_name()
        Checkout_p.input_first_name()
        Checkout_p.input_phone()

        # select payment method
        Checkout_p.select_credit_card()
        Checkout_p.click_agree_with_hotel_policy()
        Checkout_p.click_create_booking_button()

        # input card details
        Card_p.input_card_number()
        Card_p.input_card_brand()
        Card_p.input_card_expiry_date()
        Card_p.input_billing_address()
        Card_p.input_zip_code()
        Card_p.input_city()
        Card_p.input_state()
        Card_p.input_country()
        Card_p.click_pay_button()

        # validate booking complete message
        Card_p.validate_success_message()
