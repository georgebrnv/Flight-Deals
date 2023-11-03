from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "CLT"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

data = DataManager()
flight_search = FlightSearch()
sheet_data = data.get_destination_data()

if sheet_data[0]["iataCode"] == "code":
    data.fill_up_iata_codes()

for index, destination in enumerate(sheet_data):
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if sheet_data[0]["lowestPrice"] == "price" or flight.price < destination["lowestPrice"]:
        data.fill_up_lowest_price(flight, index)
