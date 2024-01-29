import random
def call():
    word="rock paper scissor"
    computerChoice=word.split()
    a=random.choice(computerChoice)
    b=str(input("inter your choice  ",))
    print()
    print("computer choice is: ",a)
    print()
    if(a==b):
        print("match draw play again")
        call()
    else:
        if(a=="rock"):
            if(b=="paper"):
                print("you won")
            else:
                print("you loss")
        elif(a=="paper"):
            if(b=="scissor"):
                print("you won")
            else:
                print("you loss")
        elif(a=="scissor"):
            if(b=="rock"):
                print("you won")
            else:
                print("you loss")
call()