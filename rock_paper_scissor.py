import random as rnd 

choices = ['rock', 'paper', 'scissor']

comp_choice = rnd.choice(choices)

play_again = 'yes'

while play_again != 'no':
    
    user_choice = str(input("Enter your choice -> rock, paper or scissor : ")).lower().strip()

    print('user choiced :' + user_choice + ' and computer choice is :'+comp_choice)

    if user_choice == comp_choice :
        print("Tie...!")
    elif comp_choice == 'rock' and user_choice == 'scissor' :
        print('computer win')

    elif comp_choice == 'rock' and user_choice == 'paper' :
        print("user win")

    elif comp_choice == 'paper' and user_choice == 'scissor':
        print('user win')

    elif comp_choice == 'scissor' and user_choice == 'paper':
       print('computer win')
    
    elif comp_choice == 'scissor' and user_choice == 'rock':
        print("user wins")
    
    elif comp_choice == 'paper' and user_choice == 'rock':
        print('computer wins')
    
    continue_game = str(input("do you want to play again (yes/no) : ")).lower()
    
    if continue_game != 'yes' :
        break

print("Mja aaya khel ke")
        
