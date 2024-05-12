'''  Connecting to the database  '''
#start by importing the sqlite3 library
import sqlite3
import time

# Set the database that we will connect to
# This is uppercase as it is constant (wont change during the program
# Make sure this file is saved in the same folder as the database
DATABASE = "Premier Leage Stats SQLite.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


get_choice = True
while get_choice:
    print("\nMenu\n=======================")
    print("1. See all items in the list")
    print("2. Add item to list")
    print("3. Delete item from list")
    print("4. Search")
    print("5. Exit")

    user_input = input("Selection: ").strip()
    print("===========\n")
    if user_input == "":
        print("Entry Cannot Be Blank")
        print("\n")
    else:
        choice = int(user_input)
        if choice not in range(1, 6):
            print("Invalid choice. Please enter a number between 1 and 5.")



        else:
            if choice == 1:
                cursor.execute("SELECT * FROM premier")
                results = cursor.fetchall()
                for i in range(len(results)):
                    print(f"{i+1}. {results[i][0]}")
                    time.sleep(0.2)


            elif choice == 2:
                break
            elif choice == 3:
                break
            elif choice == 4:
                break
            elif choice == 5:
                print("Exiting program...")
                get_choice = False  # Exit the loop







#running a query





#how to search
#Select * from premier leage where name LIKE '%_%'

