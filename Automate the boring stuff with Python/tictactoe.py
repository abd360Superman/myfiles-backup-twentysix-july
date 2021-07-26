import random
theBoard = {'top-L':' ',
'top-M':' ',
'top-R':' ',
'mid-L':' ',
'mid-M':' ',
'mid-R':' ',
'low-L':' ',
'low-M':' ',
'low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

print('You are X, Computer is O')
turn = 'x'
for i in range(9):
    if turn == 'x':
        print('X Turn. Enter position')
        move = input()
        if theBoard[move] != ' ':
            i -= 1
            continue
        theBoard[move] = 'x'
        turn = 'o'
    else:
        print('O Turn')
        temp = random.choice(list(theBoard.items()))
        move = temp[0]
        if theBoard[move] != ' ':
            i -= 1
            continue
        theBoard[move] = 'o'
        turn = 'x'
    printBoard(theBoard)
    if (theBoard['top-L'] == 'x' and theBoard['top-M'] == 'x' and theBoard['top-R'] == 'x') \
    or (theBoard['mid-L'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['mid-R'] == 'x') \
    or (theBoard['low-L'] == 'x' and theBoard['low-M'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-L'] == 'x' and theBoard['mid-L'] == 'x' and theBoard['low-L'] == 'x') \
    or (theBoard['top-M'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-M'] == 'x') \
    or (theBoard['top-R'] == 'x' and theBoard['mid-R'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-L'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-R'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-L'] == 'x'):
        print('X wins!!')
        break
    if (theBoard['top-L'] == 'o' and theBoard['top-M'] == 'o' and theBoard['top-R'] == 'o') \
    or (theBoard['mid-L'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['mid-R'] == 'o') \
    or (theBoard['low-L'] == 'o' and theBoard['low-M'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-L'] == 'o' and theBoard['mid-L'] == 'o' and theBoard['low-L'] == 'o') \
    or (theBoard['top-M'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-M'] == 'o') \
    or (theBoard['top-R'] == 'o' and theBoard['mid-R'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-L'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-R'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-L'] == 'o'):
        print('O wins!!')
        break
