import random

def computer_guess():
    x = int(input('Do you wanna I guess between 1 to...? '))
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'\nIs {guess} too high (H), too low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'\nYay! The computer guessed your number, {guess}, correctly! :)')


computer_guess()