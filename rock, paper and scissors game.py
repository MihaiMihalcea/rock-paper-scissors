import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the Rock - Paper - Scissors game!")

game_on = True

computer_options = ['rock', 'paper', 'scissors']

while game_on == True:
    player_choice = input("Let's start the game, please decide what your pick is going to be: rock, paper or scissors? ")
    computer_choice = random.choice(computer_options)
    if player_choice == 'rock':
        print("You chose rock!")
        print(rock)
        if computer_choice == 'rock':
            print("Computer chose rock!")
            print(rock)
            play_again = input("It's a tie! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'paper':
            print("Computer chose paper!")
            print(paper)
            play_again = input("You lost! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'scissors':
            print("Computer chose scissors!")
            print(scissors)
            play_again = input("You win! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
    if player_choice == 'paper':
        print("You chose paper!")
        print(rock)
        if computer_choice == 'paper':
            print("Computer chose paper!")
            print(paper)
            play_again = input("It's a tie! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'scissors':
            print("Computer chose scissors!")
            print(scissors)
            play_again = input("You lost! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'rock':
            print("Computer chose rock!")
            print(rock)
            play_again = input("You win! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
    if player_choice == 'scissors':
        print("You chose scissors!")
        print(scissors)
        if computer_choice == 'scissors':
            print("Computer chose scissors!")
            print(scissors)
            play_again = input("It's a tie! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'rock':
            print("Computer chose rock!")
            print(rock)
            play_again = input("You lost! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        if computer_choice == 'paper':
            print("Computer chose paper!")
            print(paper)
            play_again = input("You win! Would you like to play again? Y or N ")
            if play_again == 'Y':
                pass
            if play_again == 'N':
                game_on = False
        

    

