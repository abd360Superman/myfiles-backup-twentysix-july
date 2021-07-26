import random
num = random.randint(1, 100)
turns = 0
while True:
    turns = turns + 1
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You guess right')
        print('It took you %s turns' % turns)
        break
    elif i < num:
        print('Try higher')
    elif i > num:
        print('Try lower')
