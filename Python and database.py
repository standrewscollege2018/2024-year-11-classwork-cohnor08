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

# Look over results list and display one at a time

print(f"{'First Name':12} {'Last Name':15} Tutor Group")
print("="*40)

for students in results:
    print(f"{students[0]:10} {students[1]:15} {students[2]:15}")




'''
# Or this way
for i in range(len(results)):
    print(f"{results[i][0]} {results[i][1]}")
    '''



how to search
Select * from premier leage where name LIKE '%_%'





