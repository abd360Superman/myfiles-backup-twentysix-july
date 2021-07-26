import shelve

s = shelve.open('C:/Darsh Files/Automate the boring stuff with Python/The Shelve Module/test_shelf.db')
try:
    s['key1'] = {'int' : 10, 'float' : 9.5, 'string' : 'Sample Data'}
finally:
    s.close()

s = shelve.open('C:/Darsh Files/Automate the boring stuff with Python/The Shelve Module/test_shelf.db')
try:
    existing = s['key1']
finally:
    s.close()

print(existing)
