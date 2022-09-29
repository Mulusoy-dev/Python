import requests
from datetime import datetime


MY_LAT = "39.933365"
MY_LONG = "32.859741"

##############################################################################
#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#raw_data = response.json()
#print(raw_data)

#longitude = raw_data["iss_position"]["longitude"]
#print(longitude)
#latitude = raw_data["iss_position"]["latitude"]
#print(latitude)
#iss_position = (longitude, latitude)
#print(iss_position)

###############################################################################

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)





