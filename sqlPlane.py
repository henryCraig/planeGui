import sqlite3

connection = sqlite3.connect("planeData.db")

crsr = connection.cursor()

#Figure out which things i want to save in here
#I assume the things I am calling currently
crsr.execute("""CREATE TABLE tableName (
                latitude real
                longitude real
                callsign text
                countryOfOrigin text
)""")

#Maybe I should add something about the distance checked?
#It kind of seems cool to just track the airplanes right now
#So for now I guess thats fine, I can always change it later
#Timestamp








connection.commit()
connection.close()


#space
