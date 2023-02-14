# importing geopy library
from geopy.geocoders import Nominatim
#google search
from googlesearch import search
# web automation
from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def gSearch(search_query):
    # send request to Wikipedia API
    response = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=1&srsearch={search_query}')

    # parse JSON response
    data = response.json()

    # extract search results
    search_results = data['query']['search']

    # print search results
    for result in search_results:
      summary = result['snippet']
      print(f'{summary}\n')
    
def lonlat(inp):
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    # entering the location name
    getLoc = loc.geocode(inp)
    # printing address
    print(getLoc.address)
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude)
    print("Longitude = ", getLoc.longitude, "\n")

def weather(city):
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather2 = soup.select('#wob_tm')[0].getText().strip()
    
	print(time)
	print(info)
	print(weather2+"°C", "\n")
         
def main():
    inp= input("Enter the Name of City -> ")
    lonlat(inp)    
    print("Current Weather:")
    weather(inp+" weather")
    print("About "+inp)
    gSearch(inp)
    

main()