import random

print('Welcome to the Rock, Paper, Scissors game!')
print("Rock, Paper, Scissors Game Rules:\n",
      "1. Rock beats Scissors\n",
      "2. Scissors beats Paper\n",
      "3. Paper beats Rock")

options = ['Rock', 'Paper', 'Scissors']


def game():
    while True:
        user = input('Choose Rock (r), Paper (p), Scissors (s): ').lower()

        if user not in ['r', 'p', 's']:
            print("Invalid input, please enter 'r', 'p', or 's'.")
            continue

        if user == 'r':
            user_choice = 'Rock'
        elif user == 'p':
            user_choice = 'Paper'
        elif user == 's':
            user_choice = 'Scissors'

        computer_choice = random.choice(options)

        print(f'You chose {user_choice}, computer chose {computer_choice}.')

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
                (user_choice == 'Scissors' and computer_choice == 'Paper') or \
                (user_choice == 'Paper' and computer_choice == 'Rock'):
            print(f'{user_choice} beats {computer_choice}, you win!')
        else:
            print(f'{computer_choice} beats {user_choice}, computer wins!')

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again == 'n':
            print('Thanks for playing!')
            break


game()
