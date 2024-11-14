import streamClasses
import wget
import dotenv
import os
import requests

dotenv.load_dotenv() # load environment variables from .env file

# TV Shows conversion
tv_m3u_url = os.getenv("TV_M3U_URL")
i = 1
while i > 0:
    url = tv_m3u_url + str(i)
    shows_path = "m3u/apollotvshows-" + str(i) + ".m3u"
    if os.path.isfile(shows_path):
        os.remove(shows_path)
        print(f"Old version of '{shows_path}' has been deleted.")
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(wget.download(url, shows_path))
            apollo_shows = streamClasses.rawStreamList(shows_path)
            i += 1
        else:
            print(f"URL '{url}' is not valid. Status code: {response.status_code}")
            i = -1
    except requests.RequestException as e:
        print(f"Failed to reach URL '{url}'. Error: {e}")

# Movies conversion
movies_m3u_url = os.getenv(
    "MOVIES_M3U_URL"
)  # your M3U_URL variables should get set in your .env file before running
movies_path = "m3u/iptv.m3u"

if os.path.isfile(movies_path):
    os.remove(movies_path)
    print(f"Old version of '{movies_path}' has been deleted.")

print(wget.download(movies_m3u_url, (movies_path)))
apollo_movies = streamClasses.rawStreamList(movies_path)
