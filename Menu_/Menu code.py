''' This program enables users to add students to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#### Menu system for the program #######
run_program = True
while run_program:
    print("Main Menu")
    print("=========")
    print("1. Add student")
    print("2. Search for student")
    print("3. See all students")
    print("4. Quit")

    # get menu selection
    get_selection = True
    while get_selection:
        try:
            selection = int(input("Enter selection: "))
            if selection <1 or selection > 4:
                print("You must enter a number from 1-4")
            else:
                get_selection = False
        except ValueError:
            print("Only numbers from 1-4 allowed")

    # Now that we have the selection, do what the user wants

    ### Add student ###
    if selection == 1:
        print("\nAdd new student")
        # Get info about student
        first_name = input("First name: ")
        last_name = input("Last name: ")
        tutor_group = input("Tutor group: ")
        city = input("City: ")
        year_group = int(input("Year group: "))
        cursor.execute("INSERT INTO student (firstname, lastname, tutorgroup, city, yeargroup) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, tutor_group, city, year_group))
        # You must add connection.commit() or else the change will not be saved when you stop the program
        connection.commit()



    ### Search for a student ###
    elif selection == 2:
        print("\nSearch for a student")







    ### Show all students ###
    elif selection == 3:
        print("\nAll students")
        cursor.executeI("SELECT * FROM student")
        results = cursor.fetchall()
        results = [[firstname][lastname][tutorGroup]]

        for student in results:
            print(f"student[0], student[1]")


    ### Quit program ###
    else:
        run_program = False
