""" this program takes a number as input and doubles it """

# take number as a float

try:
    number = float(input("Please Enter your Number "))
except ValueError:
    print("Wrong Answer")

print(number * 2)

