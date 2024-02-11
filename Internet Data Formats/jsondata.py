import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "titale" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(count, "events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("...................\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
    print("...................\n")

    print("\nEvents that were felti:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"], feltReports, "time")


def main():

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from the server, cennot print results", webUrl.getcode())

if __name__ == "__main__":
    main()