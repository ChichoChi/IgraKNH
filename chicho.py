import random

again  = True

while (again):
        rock = 'Rock'
        paper = 'Paper'
        scissors = 'Scissors'

        izbor = input("Choose, [r]ock, [p]aper or [s]cissors : ")

        if izbor == "r":
            izbor = rock
        elif izbor == "p":
            izbor = paper
        elif izbor== "s":
            izbor = scissors
        else:
            print("Invalid Input. Try again...")

        pc_move = ""
        computer_random_number = random.randint(1, 3)

        if computer_random_number == 1:
            pc_move = rock
            print("The computer chose rock")
        elif computer_random_number == 2:
            pc_move = paper
            print("The computer chose paper")
        else:
            pc_move = scissors
            print("The computer chose scissors")

        if(izbor == rock and pc_move == scissors) or (izbor == paper and pc_move == rock) or (pc_move == scissors and pc_move == paper):
            print("You win!")
        elif(izbor == rock and pc_move == rock) or (izbor == paper and pc_move == paper) or (izbor == scissors and pc_move == scissors):
            print("Draw!")
        elif(izbor == rock and pc_move == paper) or (izbor == paper and pc_move == scissors) or (izbor == scissors and pc_move == rock):
            print("You lose!")
        tab = input("Do u want to play again : yes  or no : ")

        if tab == "yes":
            again == True
        elif tab == "no":
            again = False
            print("Thanks for playing ")
        else :
            again = False
            print("wrong input. Bye ")
