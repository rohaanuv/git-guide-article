from datetime import datetime
from pyorbital.orbital import Orbital
from pyorbital import tlefile
import requests

# Replace with your latitude and longitude
latitude = 37.7749
longitude = -122.4194

# Get the TLE data for the satellites you're interested in
response = requests.get('https://www.celestrak.com/NORAD/elements/weather.txt')
satellites = tlefile.read(response.text)

# Loop through the satellites and calculate their positions
for satellite in satellites:
    name = satellite.name
    orb = Orbital(satellite.line1, satellite.line2)
    now = datetime.utcnow()
    lon, lat, alt = orb.get_lonlatalt(now)
    
    # Calculate the distance between the satellite and your location
    distance = ((lat - latitude)**2 + (lon - longitude)**2)**0.5
    
    # If the satellite is within a certain distance of your location, print its name
    if distance < 10:
        print(name)

