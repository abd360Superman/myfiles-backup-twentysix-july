import re
passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z])                       # at least one capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9])                        # at least one numeric digit
    (?=.*[a-z])                        # at least one lower case letters
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)

print('Enter password to see if it is strong')
password = input()

mo = passwordRegex.search(password)
if not mo:
    print('Password is not strong. Make sure you use at least 8 total digits, one capital letter, one lower case letter, one numeric digit and one of !@#&*')
else:
    print('Strong password!')
