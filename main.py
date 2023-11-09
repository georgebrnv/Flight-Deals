from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "CLT"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

data = DataManager()
flight_search = FlightSearch()
sheet_data = data.get_destination_data()
notification_manager = NotificationManager()

user_data = data.subscription()

for index, destination in enumerate(sheet_data):
    if sheet_data[index]["iataCode"] == "code":
        data.fill_up_iata_codes()

    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        print(f"Nothing found for {destination}")
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms_notification(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        data.fill_up_lowest_price(flight.price, index)
