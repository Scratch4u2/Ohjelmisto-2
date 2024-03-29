import requests
from geopy.geocoders import Nominatim


def haku(hakusana):
    geolocator = Nominatim(user_agent="hakusana")
    location = geolocator.geocode(hakusana)
    apikey = "APIKEY TÄHÄN"
    if location:
        latitude = location.latitude
        longitude = location.longitude
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apikey}")
        if response.status_code == 200:
            json_data = response.json()
            print(f"Tulokset hakusanalla:{hakusana}")
            lampo_kelvin = json_data['main']['temp']
            lampo_celsius = lampo_kelvin - 273.15
            saatila = json_data['weather'][0]['description']

            print(f"Sää: {saatila.capitalize()}")
            print(f"Lämpötila celsiuksina: {lampo_celsius:.2f} °C")
        else:
            print("Error: Ei säätietoja hakusanalla")
    else:
        print("Error: Paikkaa hakusanalla ei löytynyt")


hakusana = input("Hakusana: (paikkakunta/kaupunki)\n")
haku(hakusana)