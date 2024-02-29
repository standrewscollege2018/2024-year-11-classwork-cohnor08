""" this program is a rental booking system to allocate cars by the number of seats """

import time

cars = [
    ["Suzuki Van", 2, True],
    ["Toyot'a Corolla", 4, True],
    ["Honda CRV", 4, True],
    ["Suzuki Swift", 4, True],
    ["Mitsubishi Airtrek", 4, True],
    ["Nissan DC Ute", 4, True],
    ["Toyota Previa", 7, True],
    ["Toyota Hi Ace", 12, True],
    ["Toyota Hi Ace", 12, True],
]

print("Here is a list of car's for the day")
time.sleep(3)

for i in range(len(cars)):
    available = " not"
    if cars[i][2] == True:
        available = ""
    print(
        f"{i+1}. A {cars[i][0]} is{available} available to be rented | It seats {cars[i][1]} "
    )
    time.sleep(0.2)

print()
car_temp = int(input("What Car Would You Like to Rent"))
cars[car_temp - 1][2] = False
print(cars)

for i in range(len(cars)):
    if cars[i][2] == False:
        print("Sorry that car is not availavle")













