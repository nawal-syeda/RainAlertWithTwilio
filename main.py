from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv(dotenv_path=".env")

OWM_API_KEY = os.environ.get("OWM_API_KEY")
LAT = os.environ.get("LAT")
LON = os.environ.get("LON")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")





import requests
parameters = {
    "latitude": LAT,
    "longitude": LON,
    "hourly": "weathercode",
    "forecast_days": 1
}
response = requests.get(
    "https://api.open-meteo.com/v1/forecast",params=parameters)

print(response.json())

weather_data = response.json()

going_to_rain = False
for code in weather_data["hourly"]["weathercode"][:4]:
    if code >= 51:  # 51+ means rain/drizzle/snow
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



