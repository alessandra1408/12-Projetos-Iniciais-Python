import random

def game():
    user = input("\nWhat is your choice? 'r' for rock, 'p' for paper and 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    def option():
        if computer == 'r':
            computer_option = 'rock'
        elif computer == 'p':
            computer_option = 'paper'
        else:
            computer_option = 'scissors'
        return computer_option


    if (user == 'r' or user == 'p' or user =='s'):
        if user == computer:
            print("\nIt's a tie")
        elif is_win(user, computer):
            print(f'\ncomputer: {option()}. You win!')
        else:
            print(f'\ncomputer: {option()}. You lost!')
    else:
        print(f"\nYou chose '{user}' and is not a option")


def is_win(player, opponent):
    #returns true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')or (player == 's' and opponent == 'p'):
        return True


game()