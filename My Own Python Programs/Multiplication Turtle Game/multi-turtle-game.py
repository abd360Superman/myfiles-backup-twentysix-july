import turtle
import random

finishline = turtle.Pen()
finishline.up()
finishline.forward(200)
finishline.right(90)
finishline.forward(200)
finishline.width(10)
finishline.pencolor('#000000')
finishline.down()
finishline.backward(400)
finishline.up()
finishline.left(90)
finishline.forward(20)
finishline.right(90)
finishline.down()
finishline.forward(400)
finishline.up()
finishline.left(90)
finishline.forward(20)
finishline.left(90)
finishline.down()
finishline.forward(400)

player1 = input('Enter player 1 name: ')
player2 = input('Enter player 2 name: ')

p1_wrongs = 0
p1_rights = 0
p1 = turtle.Pen()
p1.up()
p1.pencolor('#e60f0b')
p1.right(90)
p1.forward(50)
p1.left(90)
p1.down()

p2_wrongs = 0
p2_rights = 0
p2 = turtle.Pen()
p2.up()
p2.pencolor('#10e0d2')
p2.left(90)
p2.forward(50)
p2.right(90)
p2.down()

print()
print('%s red pointer and %s blue pointer' % (player1, player2))

count = 0
ans = 0
while p1_wrongs < 3 and p2_wrongs < 3 and p1_rights < 8 and p2_rights < 8:
    firstnum = random.randint(1, 999)
    secnum = random.randint(1, 999)
    product = firstnum * secnum

    count = count + 1
    if count % 2 == 0:
        ans = int(input('%s what is %s * %s? ' % (player1, firstnum, secnum)))
        if ans == product:
            p1_rights = p1_rights + 1
            p1.forward(25)
            print('You are correct!')
        else:
            p1_wrongs = p1_wrongs + 1
            print('You are wrong...')
    else:
        ans = int(input('%s what is %s * %s? ' % (player2, firstnum, secnum)))
        if ans == product:
            p2_rights = p2_rights + 1
            p2.forward(25)
            print('You are correct!')
        else:
            p2_wrongs = p2_wrongs + 1
            print('You are wrong...')

if p1_wrongs == 3:
    print('%s wins' % player2)
    print('%s loses' % player1)
elif p1_rights == 8:
    print('%s wins' % player1)
    print('%s loses' % player2)
elif p2_wrongs == 3:
    print('%s wins' % player1)
    print('%s loses' % player2)
elif p2_rights == 8:
    print('%s wins' % player2)
    print('%s loses' % player1)

    
