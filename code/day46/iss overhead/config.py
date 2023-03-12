import requests
from datetime import datetime

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=28.394857&lng=84.124008&formatted=0")
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"sunrise: {sunrise} \n sunset: {sunset}")

time_now = datetime.now().strftime("%H")

