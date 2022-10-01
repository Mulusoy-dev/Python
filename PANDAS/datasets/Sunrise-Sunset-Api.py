import requests
from datetime import datetime


MY_LAT = 39.933365
MY_LONG = 32.859741

##############################################################################

def iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    raw_data = response_iss.json()

    iss_longitude = float(raw_data["iss_position"]["longitude"])
    iss_latitude = float(raw_data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_longitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


###############################################################################
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()


    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if iss_overhead() and is_night():
    # send to email notification
    pass

