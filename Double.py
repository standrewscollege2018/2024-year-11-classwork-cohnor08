""" this program takes a number as input and doubles it """


keep_asking = True
while keep_asking:
    # take number as a float
    try:
        number = float(input("Please Enter your Number "))
        keep_asking = False
    except ValueError:
        print("Wrong Answer")

print(number * 2)
