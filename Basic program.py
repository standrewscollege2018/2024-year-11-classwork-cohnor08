#items []

get_choice = True
while get_choice == True:
    print("Menu\n=======================")
    print("1. See all items in the list")
    print("2. Add item to list")
    print("3. Delete item from list")

    try:
        choice = int(input("Selection: " ))
        if choice.strip(" ") == "":
            print("Entry Cannot Be Blank")
        else:
            get_choice = False
    except ValueError:
        print("Please Enter A Number")

if choice = <1>
print("ok")
