import requests
from flight_search import FlightSearch
import os

FLIGHTS_DATA_ENDPOINT = "https://api.sheety.co/cf65af10359d663d1010af385cb63928/flightDeals/sheet1"
USERS_DATA_ENDPOINT = "https://api.sheety.co/cf65af10359d663d1010af385cb63928/flightDeals/sheet2"
AUTH_HEADER = {
    "Authorization": os.environ.get("AUTH_BASIC_HEADER")        }
flight_search = FlightSearch()

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        sheety_response = requests.get(url=FLIGHTS_DATA_ENDPOINT, headers=AUTH_HEADER)
        self.response = sheety_response.json()

    def subscription(self):
        first_name = input("What's your first name? ")
        last_name = input("What's your last name? ")
        email1 = input("What's your EMAIL? ")
        email2 = input("Verify your EMAIL: ")
        if email1 == email2:
            user_data = {
                "sheet2": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email1
                }
            }
            response = requests.post(url=USERS_DATA_ENDPOINT, headers=AUTH_HEADER, json=user_data)
            print(f"You are in the club, {first_name}!")
            return user_data

    def get_destination_data(self):
        response = requests.get(url=FLIGHTS_DATA_ENDPOINT, headers=AUTH_HEADER)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def fill_up_iata_codes(self):
        for index, city in enumerate(self.response["sheet1"]):
            city_name = city["city"]
            iata_code = flight_search.get_iata_code(city_name)
            print(iata_code)
            sheet1_input = {
                "sheet1": {
                        "iataCode": iata_code
                }
            }
            sheet_update = requests.put(url=f"{FLIGHTS_DATA_ENDPOINT}/{index + 2}", headers=AUTH_HEADER, json=sheet1_input)
            print(sheet_update.text)

    def fill_up_lowest_price(self, price, index):
        sheet1_input = {
            "sheet1": {
                "lowestPrice": price
            }
        }
        sheet_update = requests.put(url=f"{FLIGHTS_DATA_ENDPOINT}/{index + 2}", headers=AUTH_HEADER, json=sheet1_input)
        print(sheet_update.text)
