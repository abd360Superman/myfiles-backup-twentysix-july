import pyperclip

text = {'agree': 'I agree, that sounds great!',
'thanks': 'Thanks for your help',
'signature': 'Regards, \nDarsh',
'busy': 'Not free, can we do it later?',
'greeting': 'Greetings of the day!'}

print('Enter a key to get it\'s value on clipboard')
user_key = input()

try:
    chosen = text[user_key]
    pyperclip.copy(chosen)
    print('Copied to clipboard!')
except:
    print('Invalid key')
