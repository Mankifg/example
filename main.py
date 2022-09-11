import random

player_number = 0
tries = 0

print('Welcome to guest the number game')
print('Enter maximum number')
max = int(input('>'))
find_number = random.randint(1,max)

while player_number != find_number:
    tries = tries + 1
    player_number = int(input('What number are you guesing?'))
    if player_number > find_number:
        print('[>]Your number is too big')
    if player_number < find_number:
        print('[<]Your number is too small.')

print('You guess the number')
print('It took you {} tries.'.format(tries))