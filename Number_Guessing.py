import random

number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        if(guess < number_to_guess):
            print("The number is low, guess again.")
        elif(guess > number_to_guess):
            print("Your guess is greater, try again :)")
        else:
            print("YAYY... You got it gurlll")
            break

    except ValueError:
        print("OOPS, invalid input. Try again !")

