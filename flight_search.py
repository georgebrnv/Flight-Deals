import requests
from flight_data import FlightData
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.API_KEY = os.environ.get("TEQUILA_API_KEY")
        self.SEARCH_API = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": self.API_KEY,
        }

    def get_iata_code(self, city):

        parameters = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=f"{self.SEARCH_API}/locations/query", params=parameters, headers=self.headers)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 4,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        flight_response = requests.get(url=f"{self.SEARCH_API}/v2/search", params=flight_parameters, headers=self.headers)

        try:
            data = flight_response.json()['data'][0]
        except IndexError:
            print(f"No flights found to {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_arrival"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: {flight_data.price} - {flight_data.out_date} - {flight_data.return_date}")
        return flight_data.price
