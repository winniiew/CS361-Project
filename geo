from geopy.geocoders import Nominatim
import json
geolocator = Nominatim(user_agent="TestGeolocator")

lat = float(input("Input a Latitude: "))
long = float(input("Input a Longitude: "))

location = geolocator.reverse(f"{lat}, {long}")
#location = geolocator.reverse(f"44.569754, -123.296360")

# List of keys to remove from the location output
outputClean = ["place_id", "licence", "osm_type", "osm_id", "display_name", "boundingbox"]
for nameToRemove in outputClean:
    del location.raw[nameToRemove]

# Convert the raw location to JSOON
jsonOutput = json.dumps(str(location.raw))

# Write the data to a file as jsoon
with open("locationOutput.json", "w") as f:
    f.write(jsonOutput)
