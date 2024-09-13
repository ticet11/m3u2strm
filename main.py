import streamClasses
import wget
import dotenv
import os

dotenv.load_dotenv() # load environment variables from .env file
m3u_url = os.getenv('M3U_URL') # your M3U_URL variable is set in your .env file

# for i in range(20):
#   i+=1
#   url = m3u_url + str(i)
#   shows_path = 'm3u/apollotvshows-'+str(i)+'.m3u'
#   if os.path.isfile(shows_path):
#     os.remove(shows_path)
#     print(f"Old version of '{shows_path}' has been deleted.")
#   print(wget.download(url, (shows_path)))
#   apollo_shows = streamClasses.rawStreamList(shows_path)

m3u_path = 'm3u/iptv.m3u'

if os.path.isfile(m3u_path):
  os.remove(m3u_path)
  print(f"Old version of '{m3u_path}' has been deleted.")

print(wget.download(m3u_url, (m3u_path)))
apollo_movies = streamClasses.rawStreamList(m3u_path)

