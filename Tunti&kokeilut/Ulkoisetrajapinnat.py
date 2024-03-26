import requests

response = requests.get("https://api.tvmaze.com/search/shows?q=girls")
json = response.json()
print(json[0]["show"]["name"])

def search_shows(search_query):
    response = requests.get("https://api.tvmaze.com/search/shows?q=" + search_query)
    shows = response.json()
    print(f"Tulokset hakusanalla: {search_query}")
    for show in shows:
        genres = ""
        for genre in show["show"]["genres"]:
            genres += genre + genre
        print(f"Sarja: {show["show"]['name']} - {genres} url: {show['show']['url']}")

search_input = input("Hakusana:\n")
search_shows(search_input)



