# Snake water gun

import random
game=["s","w","g"]
totalchoice=10
chances_left=0
human=0
computer=0
   

while chances_left<totalchoice :
    cinput=random.choice(game)
    userinput=input("Snake,Water,Gun:")
    if cinput==userinput :
        print("tie for both")
    elif cinput=="s" and userinput=="g" :
        human=human+1
        print("You guessed gun and computer guessed snake,gun killed snake")
        print("You win!")
        print(f"Your score is {human} and computer score is {computer}")


    elif cinput=="s" and userinput=="w":
        computer=computer+1
        print(" You guessed water and computer guessed snake,snake drank water")
        print("Computer win!")
        print(f"Your score is {human} and computer score is {computer}")
   
   
    elif cinput=="w" and userinput=="g" :
        computer=computer+1
        print("You guessed gun and computer guessed water,water destroyed gun")
        print("Computer win!")
        print( f"Your score is {human} and computer score is {computer}")
   
   
    elif cinput=="w" and userinput=="s" :
        human=human+1
        print(" You guessed snake and computer guessed water,snake drank water")
        print("You win!")
        print( f"Your score is {human} and computer score is {computer}")
   
   
    elif cinput=="g" and userinput=="s" :
        computer=computer+1
        print(" You guessed snake and computer guessed gun,gun kills the snake")
        print("computer win!")
        print( f"Your score is {human} and computer score is {computer}")    
   
   
    elif cinput=="g" and userinput=="w" :
        human=human+1
        print(" You guessed water  and computer guessed gun,water destroyed gun")
        print("You  win!")
        print(f"Your score is {human} and computer score is {computer}")    
   
   
    else :
        print("Wrong userinput")    

    chances_left=chances_left + 1
    print(f"{totalchoice-chances_left} is left out of {totalchoice} \n")

print("Game over")

if computer==human:
    print("Tie")

elif computer > human:
    print("Computer wins and you loose")

else:
    print("You win and computer loose")

print(f"Your point is {human} and computer point is {computer}")           

