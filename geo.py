from geopy.geocoders import Nominatim
import json
geolocator = Nominatim(user_agent="TestGeolocator")

lat = float(input("Input a Latitude: "))
long = float(input("Input a Longitude: "))

location = geolocator.reverse(f"{lat}, {long}")

# List of keys to remove from the location output
outputClean = ["place_id", "licence", "osm_type", "osm_id", "display_name", "boundingbox"]
for nameToRemove in outputClean:
    del location.raw[nameToRemove]

output = str(location.raw).replace("'", "\"")

# Write the data to a file as json
with open("locationOutput.txt", "wb") as f:
    f.write(output.encode("utf-8"))
