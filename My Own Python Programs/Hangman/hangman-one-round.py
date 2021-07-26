import turtle
t = turtle.Pen()

def twrong1():
    t.up()
    t.backward(150)
    t.left(90)
    t.backward(150)
    t.down()
    t.forward(435)
    t.right(90)
    t.forward(230)
    t.right(45)
    t.forward(130)
    t.right(45)

def twrong2():
    t.up()
    t.backward(3)
    t.right(90)
    t.forward(5)
    t.down()
    t.circle(50)
    
def twrong3():
    t.up()
    t.left(90)
    t.forward(100)
    t.down()
    t.forward(150)

def twrong4():
    t.up()
    t.right(180)
    t.forward(145)
    t.left(150)
    t.down()
    t.forward(115)

def twrong5():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(115)
    t.down()
    t.forward(115)

def twrong6():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(215)
    t.forward(145)
    t.right(35)
    t.down()
    t.forward(120)

def twrong7():
    t.up()
    t.right(180)
    t.forward(120)
    t.right(120)
    t.down()
    t.forward(120)


player1 = str(input('Enter first player name: '))
player2 = str(input('Enter second player name: '))

word = str(input('%s enter word for %s to guess IN LOWER CASE:' % (player1, player2)))

for x in range(0, 50):
    print('''

    ''')

answerArray = []

for i in range(0, len(word)):
    answerArray.append('_')
    i = i + 1

wrongs = 0
stringAnswer = ''
remLetters = len(word)

while remLetters > 0:
    stringAnswer = ''
    for j in answerArray:
        stringAnswer = stringAnswer + j
        stringAnswer = stringAnswer + ' '

    print(stringAnswer)

    guess = str(input('Guess a letter: '))

    prevRem = remLetters

    if len(guess) != 1:
        print(len(guess))
        print('Enter 1 letter')

    else:
        for l in range(0, len(word)):
            if word[l] == guess:
                answerArray[l] = guess
                remLetters = remLetters - 1
                
        if prevRem == remLetters:
            wrongs = wrongs + 1
            if wrongs == 1:
                twrong1()

            elif wrongs == 2:
                twrong2()

            elif wrongs == 3:
                twrong3()

            elif wrongs == 4:
                twrong4()

            elif wrongs == 5:
                twrong5()

            elif wrongs == 6:
                twrong6()

            else:
                twrong7()
                print('%s loses' % player2)
                break


if stringAnswer == word:
    stringAnswer = ''
    for m in answerArray:
        stringAnswer = stringAnswer + m    
    print(stringAnswer)
    
    print('Great Job %s' % player2)
else:
    print('Great Job %s' % player1)
    print('Word was %s' % word)
