#loop 
    # input from user - wanna play dice? (yes / no)
    # if yes:
        # generate two random numbers
        # print them
    # else if no:
        # print an end message
        # terminate the game
    # else:
        # print an error message

import random

while True:
    choice = input("Roll the dice? (y/n): ") # can also use ".lower()" --> i.e : input().lower()

    if choice == "y" or choice == "Y": # if .lower() used above, the or condition can be removed 
        one = random.randint(1,6)
        two = random.randint(1,6)
        
        print(f"{one}, {two}")

    elif choice == "n" or choice == "N": # or can be removed if used .lower()
        print("The game is over. Thank you for playing !")
        break # Program ends

    else:
        print("Invalid input bruhh")
