import calendar
import datetime
from FoundationLevelQualification.src.Pages.Locators.HomePageLocators import HomePageLocators
from FoundationLevelQualification.src.SeleniumExtended import SeleniumExtended
from datetime import date


class HomePage(HomePageLocators):
    future_string = ""

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = "https://www.clock-software.com/demo-clockpms/index.html"
        self.driver.get(home_url)

    def input_arrival_date(self):
        def add_months(sourcedate, months):
            month = sourcedate.month - 1 + months
            year = sourcedate.year + month // 12
            month = month % 12 + 2
            day = min(sourcedate.day, calendar.monthrange(year, month)[1])
            return datetime.date(year, month, day)

        today = date.today()
        future_date = add_months(today, 6)
        HomePage.future_string = future_date.strftime("%d-%m-%Y")
        self.sl.wait_and_input_text(self.ARRIVAL_BOX, HomePage.future_string)

    def input_number_of_nights(self):
        self.sl.clear_box(self.NIGHTS_BOX)
        self.sl.wait_and_input_text(self.NIGHTS_BOX, 4)

    def input_number_of_adults(self):
        self.sl.clear_box(self.ADULTS_BOX)
        self.sl.wait_and_input_text(self.ADULTS_BOX, 4)

    def input_number_of_children(self):
        self.sl.clear_box(self.CHILDREN_BOX)
        self.sl.wait_and_input_text(self.CHILDREN_BOX, 1)

    def click_book_now(self):
        self.sl.wait_and_click(self.BOOK_NOW_BTN)

    def store_test_text(self):
        test_text = self.sl.wait_and_get_text(self.TEST_TEXT)
        print(f"Test text is: {test_text}")
