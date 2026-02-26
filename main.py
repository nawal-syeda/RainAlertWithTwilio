
from twilio.rest import Client
import os
OWM_API_KEY = os.environ.get("OWM_API_KEY")
LAT = os.environ.get("LAT")
LON = os.environ.get("LON")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")




import requests
parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": OWM_API_KEY,
    "cnt":4
}
response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
going_to_rain = False
for item in weather_data["list"]:
    if item["weather"][0]["id"]<700:
        going_to_rain = True
if going_to_rain:
    print("bring an umbrella")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="It's going to rain in the next few hours, don't forget to bring an umbrella.",
        from_=TWILIO_FROM_NUMBER,
        to=TWILIO_TO_NUMBER,
    )

    print(message.body)
    print(message.status)

