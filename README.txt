This assignment contains my own framework for writing an automated test case for the provided
website

It contains an end to end test case for booking a specific type of room and validatiing tge booking information 
Each page of the website is split into different pages of the project
Each page contains a class which contain functions related to that page in the test 
Locators also have their own page to make the different page tabs look neater
The test runs by creating an object of each page class in the main test tab and calling the required functions of the class

Home page involves navigating to the url, inputting booking information such as date, amounts of nights stay, amount of adults, etc. 
Room page involves selecting the specific room 
Extra services page involves selecting any services required to further validate at the checkout page 
Checkout page involves verifying all data matches the inputted information, and inputting contact info and selecting payment info 
Card page involves inputting payment info and finallising the checkout process including validating a successful booking message

test_end_to_end_book_hotel_room.py is the main test case 
