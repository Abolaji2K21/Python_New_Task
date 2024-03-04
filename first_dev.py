import requests

# url = "https://api.openweathermap.org/data/2.5"
# url2 = ("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,"
#         "wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
# r = requests.get(url2)
#
# # r1 = requests.get(url)
#
# print(r.text)

# # print(r1.text)
# data = r.json()
# print(data['current_units']['time'])
#
# print(data['current_units'])
# print(data)

url3 = ("https://media.licdn.com/dms/image/D4D03AQEqAKmfIfxYVg/profile-displayphoto-shrink_800_800/0/1690304358450?e"
        "=1715212800&v=beta&t=vUUPM722dVEkUuoQlBilCsvv5r7cWyZcwueEEjsv77g")
r5 = requests.get(url3)

with open('jumong.png', mode='wb') as mf:
    mf.write(r5.content)
