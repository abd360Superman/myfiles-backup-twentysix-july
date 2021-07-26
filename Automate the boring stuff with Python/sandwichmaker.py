import pyinputplus as pyip
bread = pyip.inputMenu(prompt='Choose bread type: \n', choices=['wheat', 'white', 'sourdough'], numbered=True)
protein = pyip.inputMenu(prompt='Choose protein type: \n', choices=['chicken', 'turkey', 'ham', 'tofu', 'egg'], numbered=True)
cheese = pyip.inputYesNo(prompt='Do you want cheese? \n')
if cheese == 'yes':
    global cheeseType
    cheeseType = pyip.inputMenu(prompt='Which cheese type do you want? \n', choices=['cheddar', 'swiss', 'mozzarella'], numbered=True)
sauce = pyip.inputMenu(prompt='Which sauce do you want? \n', choices=['ketchup', 'mayo', 'mustard'], numbered=True)
veggie = pyip.inputMenu(prompt='Whice veggie do you want? \n', choices=['tomato', 'lettuce'], numbered=True)
many = pyip.inputNum(prompt='How many such sandwiches do you want? \n')
sandwichname = bread + ' bread ' + protein + ' '
if cheese == 'yes':
    sandwichname += cheeseType + ' cheese in '
sandwichname += sauce + ' with ' + veggie + ' sandwich'
print('Your order: %s %s' % (str(many), sandwichname))
