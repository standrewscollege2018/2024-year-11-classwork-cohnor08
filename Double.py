""" this program takes a number as input and doubles it """


#start a loop for error catching

keep_asking = True
while keep_asking:
    # take number as a float and double it
    try:
        number = float(input("Please Enter A Postive Number "))
        if number >=0:
            keep_asking = False
        else:
           print("Please Enter A Postive Number")


    except ValueError:
        print("Wrong Answer")

# print the rrsult
print(f"{number} doubled is {number * 2}")



