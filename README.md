# Flight-Deals
This code finds cheapest flights and store these data in Google Sheets Table.

1. Create a Google Sheet Table the way is shown below (type in cities only, for "IATA Code" use "code", for "Lowest Price" use "price"):

```
  1 | City    | IATA Code | Lowest Price
  2 | [city1] | code      | price
  3 | [city2] | code      | price
   etc...
```

3. Use Sheety.co API, create you account and use your own API and Basic Authentication Header.
4. Use Tequila.kiwi.com to find all data we need flight-wise, sign up and use your own API_KEY.
5. In main.py set your own ORIGIN_CITY_IATA location code (where your trip starts from).
6. In notification_manager.py use your own ACCOUNT_SID, AUTH_TOKEN, PHONE_FROM and PHONE_TO by signing up on TWILIO.COM

---
PARAMETERS:
- You can change flight parameters through flight_parameters dictionary in flight_search.py 

---
MAKE SURE:
1. To spell cities name in Google Sheet correctly.
2. To spell ORIGIN_CITY_IATA code correctly.

