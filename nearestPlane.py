#silver
#https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/

#eiffel tower coordinates for example purposes
#48.8584° N, 2.2945° E

#positive longitude is N, negative is S
#positive Latitude is EAST, negative longitude is WEST

#latitude is written before longitude

"""
Geodesic distance
Callsign - DONE
Lattitude and Longitude - DONE
Geometric Altitude - DONE
Country of origin - DONE
ICAO24 ID - DONE
"""

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

    print("Closest Distance: ", closestPlaneDistance)
    print("Longitude: ", closestPlaneNumber.longitude)
    print("Latitude: ", closestPlaneNumber.latitude)
    print("Geometric Altitude: ", closestPlaneNumber.geo_altitude)
    print("Country of Origin: ", closestPlaneNumber.origin_country)
    print("Callsign: ", closestPlaneNumber.callsign)
    print("ICA024 ID: ", closestPlaneNumber.icao24)


#eiffelTower = (48.8584, -71.312796)
findClosestPlane(48, -71)




#NOTE: Latitudes range from 0 to 90. Longitudes range from 0 to 180
#the user inputs should be within these ranges



#will take two strings
#48.8584 N
#2.2945 E

#if there is a space take the letter afterward?

#the first thing I want to do is figure out how to get the distance of two locations using geopy

#def distanceFinder(latitude, longitude):

"""
if latitude greater than 90 or less than -90
if longitude greater than 180 or less than -180
"""
