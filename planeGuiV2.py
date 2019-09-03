from tkinter import ttk
from tkinter import *
import re
import time

from opensky_api import OpenSkyApi
from geopy import distance

def findClosestPlane(givenLat, givenLon):
    closestPlaneDistance = 100000
    poi = (givenLat, givenLon)
    api = OpenSkyApi()
    states = api.get_states()
    for s in states.states:
        currentPlane = (s.latitude, s.longitude)
        currentPlaneDistance = distance.geodesic(poi, currentPlane, ellipsoid ='GRS-80').miles
        if float(currentPlaneDistance) < float(closestPlaneDistance):
            closestPlaneDistance = currentPlaneDistance
            closestPlaneNumber = s

    #print("Closest Distance: ", closestPlaneDistance)
    #print("Longitude: ", closestPlaneNumber.longitude)
    #print("Latitude: ", closestPlaneNumber.latitude)
    #print("Geometric Altitude: ", closestPlaneNumber.geo_altitude)
    #print("Country of Origin: ", closestPlaneNumber.origin_country)
    #print("Callsign: ", closestPlaneNumber.callsign)
    #print("ICA024 ID: ", closestPlaneNumber.icao24)

    return [closestPlaneDistance, closestPlaneNumber.latitude, closestPlaneNumber.longitude, closestPlaneNumber.callsign, closestPlaneNumber.origin_country]

def findPlaneCallback():
    if (latEntry.get().isdigit() == True) and (longEntry.get().isdigit() == True):
        latInt = int(latEntry.get())
        longInt = int(longEntry.get())

        if 90 >= latInt >= 0:
            if 180 >= longInt >= 0:
                textReturn.replace("1.0", "end", "Calling...")

                planeReturnList = findClosestPlane(latInt , longInt)

                #textReturn.replace("1.0", "end", latEntry.get() + "\n" + longEntry.get())
                textReturn.replace("1.0", "1.end", "Closest Distance: " + str(planeReturnList[0]) + "\n")
                textReturn.replace("2.0", "2.end", "Latitude: " + str(planeReturnList[1]) + "\n")
                textReturn.replace("3.0", "3.end", "Longitude: " + str(planeReturnList[2]) + "\n")
                textReturn.replace("4.0", "4.end", "Call Sign: " + str(planeReturnList[3]) + "\n")
                textReturn.replace("4.0", "4.end", "Country of Origin: " + str(planeReturnList[4]))

            else:
                textReturn.replace("1.0", "end", "Please enter a longitude between 180 and 0")
        else:
            textReturn.replace("1.0", "end", "Please enter a latitude between 90 and 0")
    else:
        textReturn.replace("1.0", "end", "Please Enter numbers in both entry points")


root = Tk()

latLabel = Label(root, text = "Lat:")
latLabel.pack()
latEntry = ttk.Entry(root, width = 30)
latEntry.pack()
longLabel = Label(root, text = "Long:")
longLabel.pack()
longEntry = ttk.Entry(root, width = 30)
longEntry.pack()

findPlaneButton = ttk.Button(root, text = "Find Plane")
findPlaneButton.pack()
textReturn = Text(root, width = 40, height = 10)
textReturn.pack()



findPlaneButton.config(command = findPlaneCallback)


#Latitudes range from 0 to 90. Longitudes range from 0 to 180


root.mainloop()
