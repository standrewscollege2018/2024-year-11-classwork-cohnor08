'''Starter'''


def multiply():

keep_asking = True
while keep_asking:

    try:
        Num1 = float(input("Please Enter First Number"))

        Num2 = float(input("Please Enter Second Number"))
    except ValueError:
        print("Try again")


