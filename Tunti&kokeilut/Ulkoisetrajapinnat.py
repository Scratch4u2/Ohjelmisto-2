import requests

response = requests.get("https://api.tvmaze.com/search/shows?q=girls")
json = response.json()
print(json[0]["show"]["name"])

for show in json:
    print(show["show"]["name"])



