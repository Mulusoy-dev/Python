import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()



raw_data = response.json()
print(raw_data)

longitude = raw_data["iss_position"]["longitude"]
print(longitude)
latitude = raw_data["iss_position"]["latitude"]
print(latitude)
iss_position = (longitude, latitude)
print(iss_position)


