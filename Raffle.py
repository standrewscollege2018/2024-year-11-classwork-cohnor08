""" This program takes a input of names and then randomly picks one for the raffle"""

# inputs the package random
import random

# creates a list called names
names = []

# get prize
prize = input("What is the prize for your raffle ")

# get value from input
# Try and Except
get_value = True
while get_value == True:
    try:
        value = float(input("Enter value:"))
        get_value = False
    except ValueError:
        print("Please Enter a Number")



# welcome message
print("Please enter the names who will be participating, and press enter!")
# repeat forever untill keep_asking equals false
keep_asking = True
while keep_asking:
    # gets a input
    get_name = input("")

    # if end is entered break
    if get_name.lower() == "end":
        keep_asking = False

    # put inputted names into list
    else:
        names.append(get_name)

# random library
r = random.randint(0, len(names) - 1)

# Print the random name from list
print(f"Good Job {names[r]}, you won {prize}! ")
