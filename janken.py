import random

def opponent(x):
    x : int = random.randint(1,3)

    return x

user : input = input("rock, paper, scissor?")

choice : dict = {"rock":1,
                 "paper":2
                 "scissor":3}

if (int(input)==1):
    pass