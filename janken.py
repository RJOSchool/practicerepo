import random

def opponent() -> int:
    x : int = random.randint(1,3)

    return x

user : str = input("rock, paper, scissor?").lower()

choice : dict = {"rock":1,
                 "paper":2,
                 "scissor":3}

opponentschoice : int = opponent()
userschoice : int = choice.get(user)

if userschoice is None:
    print("Invalid input. Please choose 'rock', 'paper', or 'scissor'.")
else:
    print(f"You chose {user}, and the opponent chose {list(choice.keys())[list(choice.values()).index(opponentschoice)]}.")

    # Determine the winner
    if userschoice == opponentschoice:
        print("It's a tie!")
    elif (userschoice == 1 and opponentschoice == 3) or \
         (userschoice == 2 and opponentschoice == 1) or \
         (userschoice == 3 and opponentschoice == 2):
        print("You win!")
    else:
        print("You lose!")