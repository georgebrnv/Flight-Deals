from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_FROM = os.environ.get("TWILIO_PHONE_FROM")
PHONE_TO = os.environ.get("TWILIO_PHONE_TO")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms_notification(self, message):
        message = self.client.messages.create(
            from_=PHONE_FROM,
            to=PHONE_TO,
            body=message
        )
        print(message.sid)
