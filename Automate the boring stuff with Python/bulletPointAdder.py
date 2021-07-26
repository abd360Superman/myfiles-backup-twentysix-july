#! python3
# bulletPointAdder.py - Adds Bullet points to what you paste

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
