print('Enter the number of numbers that need to be bubble sorted')
x = int(input())

numbers = []
write_numbers = []
i = 0
while i < x:
    print('Enter number')
    n = input()
    write_numbers.append(n)
    numbers.append(int(n))
    i += 1

def listToString(l, s):
    for q in range(x):
        temp = str(l[q])
        s += temp
        s += ', '
    return s

write_numbers_string = ' '
append_unsorted = open('records.txt', 'a+')
append_unsorted.write('\nNew Entry. Unsorted numbers: \n')
append_unsorted.write(listToString(write_numbers, write_numbers_string))
append_unsorted.close()

print('List you entered')
print(numbers)

def bubblesort(l):
    swapped = None
    for a in range(x):
        swapped == False
        for b in range(x-a-1):
            if l[b] > l[b+1]:
                l[b], l[b+1] = l[b+1], l[b]
                swapped == True
        if swapped == False:
            break

bubblesort(numbers)

print('Bubble Sorted List')
print(numbers)

write_numbers_string = ' '
write_numbers = numbers
append_sorted = open('records.txt', 'a+')
append_sorted.write('\nSorted numbers: \n')
append_sorted.write(listToString(write_numbers, write_numbers_string))
append_sorted.close()
