import time

import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage

MY_LAT = 51.812565
MY_LONG = 5.837226

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_longitude, iss_latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_hour = time_now.hour

is_overhead = False

while not is_overhead:
    time.sleep(60)
    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5 and (time_hour > sunset or time_hour < sunrise):
        my_email = "ruidongsmile@outlook.com"
        password = "1123581321Dr"
        message_info = "The ISS is above your head now!"

        msg = EmailMessage()
        msg.set_content(message_info)

        msg['Subject'] = 'ISS is coming!'
        msg['From'] = my_email
        msg['To'] = 'ruidongshuai@gmail.com'

        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)

        is_overhead = True