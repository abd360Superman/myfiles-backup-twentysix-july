import re
beginsWithLetter = re.compile(r'^s')
endsWithNumber = re.compile(r'\d$')
print('Enter text to see if starts with letter and ends with nuber')
text = input()
print(beginsWithLetter.search(text))
print(endsWithNumber.search(text))
