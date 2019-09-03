#Latitudes range from 0 to 90. Longitudes range from 0 to 180

givenLatitude = 92
givenLongitude = 60


#Alright so this does work
if 90 >= givenLatitude >= 0:
    print("given latitude works!")
else:
    print("bad latitude, please re-enter")

if 180 >= givenLongitude >= 0:
    print("given longitude works!")
