import pprint
pprint.pprint('Enter message to know character details')
message = input()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)
