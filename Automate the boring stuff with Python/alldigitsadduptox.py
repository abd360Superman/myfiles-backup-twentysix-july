import pyinputplus as pyip
count = pyip.inputNum(prompt='Enter num to check whether the number you enter later, it\'s digits add up to this number: ')
def addsuptox(number):
    numberList = list(number)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != count:
        raise Exception('The digits must add up to %s, not %s' % (count, sum(numberList)))
    return int(number)

print('Start entering number')
response = pyip.inputCustom(addsuptox)
print(response)
