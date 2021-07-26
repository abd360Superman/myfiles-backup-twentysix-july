ay = 2
bee = int(input('Enter number to get prime factorized: '))

while bee != 0:
    y = bee / ay
    x = int(y)

    if y == x and y != 1:
        print('%s x' % ay)
        bee = y
    elif y == 1:
        print('%s' % bee)
        break
    else:
        ay = ay + 1
