from tkinter import *

#Also I feel like I could sketch this thing out first


#Appears to be useful to deal with a greyed out box
#https://stackoverflow.com/questions/51781651/showing-a-greyed-out-default-text-in-a-tk-entry


root = Tk()
Label(root, text="Latitude").grid(row=0)
Label(root, text="Longitude").grid(row=1)

latEntry = Entry(root)
longEntry = Entry(root)

latEntry.grid(row=0, column=1)
longEntry.grid(row=1, column=1)

findPlaneButton = Button(root, text = "Find Plane")
findPlaneButton.grid(row = 2, column = 0, columnspan = 2)

textReturn = Text(root, width = 20, height = 5)
textReturn.grid(row = 3, column = 0, columnspan = 2, sticky = W+E+N+S)




mainloop( )
