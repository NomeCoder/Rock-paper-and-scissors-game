#fucking rock, paper scissors game
import random



def rnd():
    options=("rock", "paper", "scissors")
    return random.choice(options)
x=rnd()    




user_inp=str(input("YOUR TURN"))

if user_inp==("rock") and x==("paper"):
    print("comp won")
elif user_inp==("rock") and x==("scissor"):
    print("user won")
elif user_inp==("rock") and x==("rock"):
    print("tie")   
elif user_inp==("paper") and x==("paper"): 
    print("tie")
elif user_inp==("paper") and x==("scissors"):
    print("comp won")
elif user_inp==("paper") and x==("rock"):
    print("user won") 
elif user_inp==("scissors") and x==("paper"):
    print("user won")
elif user_inp==("scissors") and x==("scissors"):
    print("tie")
elif user_inp==("scissors") and x==("rock"):
    print("comp won")           

