'''  Example of connecting to a database and running queries  '''
#start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
# This is uppercase as it is constant (wont change during the program
# Make sure this file is saved in the same folder as the database
DATABASE = "Students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT firstName, lastName, tutorGroup FROM student LIMIT 5")

results = cursor.fetchall()
