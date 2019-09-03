#using this vid - https://www.youtube.com/watch?v=pd-0G0MigUA
#part of the standard library which is useful
import sqlite3

#first we have to connect to the database
connection = sqlite3.connect("myTable.db")

#Theres a connection cursor apparently?
#This thing is acting like the cursor in our sql file
#It allows us to manipulate that file, store, retrieve, etc.
crsr = connection.cursor()

#SQL command to create a table in the database
#sql_command =

#This will create an employee table inside myTable.db
#This is going to be wrapped in three quotes, which is called something like a "doc-string", or "dot-string"
#Allows us to write a string with multiple lines that requires no special breaks
#It is called docstring
crsr.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay real
)""")

#This will save the changes in the table.db file, otherwise we wont see the changes, because they wont have been finalized
connection.commit()

#Its good practice to close the connection each time you use it
connection.close()


#5 data types to work with here in sql
#Null, integer, real text, blob
#Real is a floating point value, can be useful for dollar amounts, finances, etc.
