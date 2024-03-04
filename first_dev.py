import requests

# url = "https://api.openweathermap.org/data/2.5"
url2 = ("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,"
        "wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
r = requests.get(url2)

# r1 = requests.get(url)

print(r.text)
# print(r1.text)
data = r.json()
print(data['current_units']['time'])

print(data['current_units'])
print(data)

