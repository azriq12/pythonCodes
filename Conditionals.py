"""
Your module description
"""
userReply = input("Do you need a room? (Key in Y or N) ")
if userReply=="Y":
    print("Welcome.")
    userReply= input("Would you like a single room, deluxe room or royal suite? (Key in SR, DR, or RS. Press ENTER to exit)")
    if userReply=="SR":
        print("The room costs RM237 per night.")
    elif userReply=="DR":
        print("The room costs RM471 per night.")
    elif userReply=="RS":
        print("The room costs RM3933 per night.")
    else:
        print("Thank you for your visit.")
else:
    print("GET OUT!")

