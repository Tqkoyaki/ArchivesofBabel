# In this assignment you will write a Python program somewhat similar to
# [http://www.py4e.com/code3/geojson.py]. The program will prompt for a location,
# contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID is a textual identifier
# that uniquely identifies a place as within Google Maps.
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Setups the API key and the service URL for data retrieval
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Takes location as input
address = input('Enter location: ')

# Connects to API
parms = dict()
parms['key'] = api_key
parms['address'] = address
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

# Gets data and converts to JSON
url = urllib.request.urlopen(url, context=ctx)
data = url.read().decode()
print('Retrieved', len(data), 'characters')
data = json.loads(data)

# Parses JSON and prints place ID
print('Place id', data["results"][0]["place_id"])