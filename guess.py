import random as rd
maxrd = 20
halfMaxrd = int(maxrd/2)
tries = 10
halfTries = int(tries/2)
hints = {"odd": True, "half": True}
guessNum = rd.randint(0, maxrd)

print("You have 10 tries to guess a whole number between 0 and 20. q to quit")
while tries > 0:
    # ERROR CHECK AND ABORT GAME
    ii = input("Type a number between 0 and 20: ")

    if ii == "q" or ii == "Q":
        print("Game aborted")
        break
    else:  # CONVERT INPUT TO INTEGER  ELSE THROW ERROR MESSAGE AND LOOP
        try:
            n = int(ii)
        except ValueError as e:
            print("Invalid input. Type a number.")
            continue

    # WIN CONDITION
    if n == guessNum:
        print("\nYou guessed correct. YOU WIN!!")
        print(f"Number is {guessNum}")
        print("*" *45)
        print()
        playAgain = input("Play again? (y / n) :")
        if playAgain == "y":
            tries = 10
            hints = {"odd": True, "half": True}
            guessNum = rd.randint(0, maxrd)
            continue
        else:
            print("PLAYER HAS STOPPED GAME")
            break
            
    # LOSE CONDITION
    elif tries == 1 and n != guessNum:
        print("\nYour 10 tries expired. \nGAME  OVER")
        print("*" *45)
        #tries = 0
        playAgain = input("Play again? (y / n) :")
        if playAgain == "y":
            tries = 10
            hints = {"odd": True, "half": True}
            guessNum = rd.randint(0, maxrd)
            continue
        else:
            print("PLAYER HAS STOPPED GAME")
            break
            
    # GAME IN PROGRESS
    else:
        tries -= 1
        print(f"\n INCORRECT. Remaining tries = {tries}. Try again.")
        if tries > halfTries and tries < 8 and hints["half"] == True:
            hints["half"] = False
            if guessNum <= halfMaxrd:
                print(f"Number is less than {halfMaxrd + 1}")
            else:
                print(f"Number is more than {halfMaxrd}")
        elif tries < halfTries and hints["odd"] == True:
            hints["odd"] = False
            if guessNum % 2 == 0:
                print("Number is even")
            else:
                print("Number is odd")
        print("_" *45)
        
