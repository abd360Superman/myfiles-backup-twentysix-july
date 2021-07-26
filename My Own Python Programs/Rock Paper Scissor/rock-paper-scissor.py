import random

print('Rock Paper Scissors!')
winscore = int(input('What is the winning score? '))

comp_score = 0
player_score = 0

def check_action(x):
    if x == 0:
        return 'rock'
    elif x == 2:
        return 'scissor'
    elif x == 5:
        return 'paper'

rounds = 0

while player_score < winscore or comp_score < winscore:
    rounds += 1
    print('Round %s' % rounds)
    
    choice = int(input('Enter 0 for rock, 2 for scissor and 5 for paper: '))
    if choice != 0 and choice != 2 and choice != 5:
        choice = int(input('Enter 0 for rock, 2 for scissor and 5 for paper: '))
        
    comp_choices = [0, 2, 5]
    comp_choice = comp_choices[random.randint(0, 2)]

    player_string = check_action(choice)
    comp_string = check_action(comp_choice)
    print('Your action: %s' % player_string)
    print('Computer action: %s' % comp_string)

    if (choice == 0 and comp_choice == 2) or (choice == 2 and comp_choice == 5) or (choice == 5 and comp_choice == 0):
        player_score += 1
        print('Player wins round and get\'s a point! ')
    elif (comp_choice == 0 and choice == 2) or (comp_choice == 2 and choice == 5) or (comp_choice == 5 and choice == 0):
        comp_score += 1
        print('Computer wins round and get\'s a point! ')
    else:
        print('Draw Round')

    print('Player score: %s' % player_score)
    print('Computer score: %s' % comp_score)

    print(' ')

if player_score >= winscore:
    print('Player wins!')

if comp_score >= winscore:
    print('Computer wins!')
