import requests
from flight_search import FlightSearch
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTH_HEADER = {
            "Authorization": os.environ.get("AUTH_BASIC_HEADER"),
        }
flight_search = FlightSearch()

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=AUTH_HEADER)
        self.response = sheety_response.json()

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=AUTH_HEADER)
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
            sheet_update = requests.put(url=f"{SHEETY_ENDPOINT}/{index+2}", headers=AUTH_HEADER, json=sheet1_input)
            print(sheet_update.text)

    def fill_up_lowest_price(self, price, index):
        sheet1_input = {
            "sheet1": {
                "lowestPrice": price
            }
        }
        sheet_update = requests.put(url=f"{SHEETY_ENDPOINT}/{index + 2}", headers=AUTH_HEADER, json=sheet1_input)
        print(sheet_update.text)
