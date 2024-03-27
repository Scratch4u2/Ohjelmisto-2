import requests
from geopy.geocoders import Nominatim

def haku(hakusana):
    geolocator = Nominatim(user_agent="hakusana")
    location = geolocator.geocode(hakusana)
    latitude = location.latitude
    longitude = location.longitude
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=cf7e316ea8b13f6f70d3db522bcec441")
    json = response.json()
    print("Tulokset hakusanalla:", hakusana)
    print(json)
hakusana = input("Hakusana: (paikkakunta/kaupunki)\n")
haku(hakusana)