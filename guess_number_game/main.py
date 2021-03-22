import random

print('-----------------------------')
print('   GUESS THAT NUMBER GAME')
print('-----------------------------')
print()

the_number = random.randint(0, 100)

name = input('Player what is your name? ')
guess = -1

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print("Sorry {1}, your guess  of {0} was too low".format(guess, name))
    elif guess > the_number:
        print("Sorry {1}, your guess of {0} was too high".format(guess, name))
    else:
        print('Excellent work {1}, you won, it was {0}'.format(guess, name))

print('done')
