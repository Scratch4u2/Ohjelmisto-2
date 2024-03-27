import requests
from geopy.geocoders import Nominatim


def haku(hakusana):
    geolocator = Nominatim(user_agent="hakusana")
    location = geolocator.geocode(hakusana)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={APIKEY TÄNNE}")
        if response.status_code == 200:
            json_data = response.json()
            print("Tulokset hakusanalla:", hakusana)
            temperature_kelvin = json_data['main']['temp']
            lampo_celsius = temperature_kelvin - 273.15
            saatila = json_data['weather'][0]['description']

            print(f"Sää: {saatila.capitalize()}")
            print(f"Lämpötila celsiuksina: {lampo_celsius:.2f} °C")
        else:
            print("Error: Ei säätietoja hakusanalla")
    else:
        print("Error: Paikkaa hakusanalla ei löytynyt")


hakusana = input("Hakusana: (paikkakunta/kaupunki)\n")
haku(hakusana)