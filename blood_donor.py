""" this program assesses whether or not a blood donor is eligible for blood"""

'''this function check() checks to see if the user input is an integer'''
def check(a):
    try:
        a = int(a)
        return True
    except ValueError:
        return False


get_age = True
while get_age == True:
    age = input("Age")
    if check(age):
        get_age = False
    else:
        print("Oops")


get_weight = True
while get_weight == True:
    weight = input("Weight")
    if check(weight):
        get_weight = False
    else:
        print("Opps")

