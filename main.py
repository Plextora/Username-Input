username = input("Type a username: ")


if len(username) < 3:
    print("Name must be at least 3 characters.")
elif len(username) > 10:
    print("Name must be a maximum of 10 characters.")
else:
    print("That username looks snazzy!")