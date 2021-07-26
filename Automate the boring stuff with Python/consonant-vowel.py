import re
print('Enter text to know the vowels and consonants entered')
text = input()
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(text))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall(text))
