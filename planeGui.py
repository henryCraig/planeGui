#adding a GUI to the nearestPlane program

from tkinter import *
from tkinter import ttk
import re
root = Tk()

latitudeEntry = ttk.Entry(root, width = 30)
longitudeEntry = ttk.Entry(root, width = 30)
latitudeEntry.pack()
longitudeEntry.pack()

button = ttk.Button(root, text = "Find Plane")
button.pack()

textReturn = Text(root, width = 40, height = 10)
textReturn.pack()



#stack overflow sugggests using regex instead of isdigit, because it wont accept the . in a float
#automate the boring stuff

def callback():
    if latitudeEntry.get() == "" or longitudeEntry.get() == "":
        textReturn.replace("1.0", "end", "Please input both Latitude and Longitude")
    elif latitudeEntry.get().isdigit() == False or longitudeEntry.get().isdigit() == False:
        textReturn.replace("1.0", "end", "Please insert appropriate coordinates")
    else:
        textReturn.replace("1.0", "end", latitudeEntry.get() + "\n" + longitudeEntry.get())
button.config(command = callback)



root.mainloop()
