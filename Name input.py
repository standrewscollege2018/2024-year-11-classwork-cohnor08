#Set Up list
names = []

#Start Asking For Names
keep_asking = True
while keep_asking:
    # Get names
    name = input()
    # if user enters stop then end loop by making keep_asking False
    if name.lower() == "stop":
       keep_asking = False
    elif name.strip(" ") == "":
        print("No Blanks Allowed")
    else:
        names.append(name)

    # Order Names into alphabetical order
    names = sorted(names)

