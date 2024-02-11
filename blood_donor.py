""" this program assesses whether or not a blood donor is eligible for blood"""

keep_asking = True
while keep_asking == True:

    try:

        age = float(input("Please Enter Your Age"))
        weight = float(input("Please Enter Your Weight"))

        if age >= 16 and weight >= 50:
            print("You Are Eligible")
        else:
            print("You Are Not ELigible")

        keep_asking = False
    except ValueError:
        print("Try again")
