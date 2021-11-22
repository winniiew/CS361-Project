# CS361 Assignment 7
# Author: Winnie Woo
# Date: 11/11/2021


from geopy.geocoders import Nominatim
import json
import wikipedia

url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="

def getCityInfoFromLatLong():
    geolocator = Nominatim(user_agent="TestGeolocator")

    lat = float(input("Input a Latitude: "))
    long = float(input("Input a Longitude: "))

    location = geolocator.reverse(f"{lat}, {long}")

    # List of keys to remove from the location output
    outputClean = ["place_id", "licence", "osm_type", "osm_id", "display_name", "boundingbox"]
    for nameToRemove in outputClean:
        del location.raw[nameToRemove]

    return json.loads(str(location.raw).replace("'", "\""))


def display_info(cityInfo):
        """
        Takes input as a query and writes result to search_result.txt
        Uses Wikipedia to search and return a summary of text related to search query
        """

    # If the returned location doesn't have a city name pull the county instead
    if "city" in cityInfo["address"]:
        cityQuery = cityInfo["address"]["city"].strip() + "," + cityInfo["address"]["state"]
    else:
        print("No city name found, the county in which these coordinates are located was used instead")
        cityQuery = cityInfo["address"]["county"].strip() + "," + cityInfo["address"]["state"]

    # search wikipedia, parse data, and write summary to search_result.txt
    summary = wikipedia.summary(cityQuery)
    #print(summary)
    r_dict = {'name':cityQuery, 'summary':summary, 'location_info':cityInfo}

    with open("wiki_result.txt", "w") as outfile:
        json.dump(r_dict, outfile)


if __name__ == "__main__":

    # Reverse geocode the lat/long to get the location information
    cityInfo = getCityInfoFromLatLong()

    display_info(cityInfo)
    print("Output written to file!")
