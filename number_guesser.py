def main():

    import random

    # welcome message 
    welcome_message = "Welcome to my game.\nYou only have 3 tries to guess a number between 1 and 10"
    print(welcome_message)

    # the random number picked by the algorithm 
    winning_number  = random.randint(0,10)

    # players total number of tries
    players_tries = 3

    print("****************************************************")

    # part that actually does something
    
    while players_tries > 0:
        
        guess = int(input("what is your guess?\n"))
        
        
        if guess == winning_number:
            print("Correct")

            break

        else:
            players_tries -=1
            print(f"Incorrect.You have {players_tries} tries ramaining")

            

        if players_tries == 0:
            print("Game over")

            break

    again = input("Would want to go again? y/n \n")

    if again == "y":
        print("Doing stuff...")
        main()

    else:
        print("Goodbye")
        exit()

main()

  

    