import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
json = response.json()
print(json["value"])


