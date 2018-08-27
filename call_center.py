"""Pizza call-center.

Menu of pizza was taken from:
http://www.johnspizzerianyc.com/Times-Square-Menu/Pizza

"""

# HERE IS THE CONTENT THAT WE GONNA USE>>>>

import random
import re
import json

menu_full = '''
    Here is our full menu!

    Traditional:
    Mozzarella cheese and tomato sauce.
    Price - 19$

    Margherita:
    Fresh mozzarella cheese, tomato sauce and basil.
    Price - 22$

    Pizza Bianca:
    Ricotta and mozzarella cheeses (No tomato sauce).
    Price - 21$

    Marinara:
    Tomato sauce, fresh garlic and basil (No cheese).
    Price - 17$

    Havaiian Pizza:
    Mozzarella cheese, tomato sauce, ham and pineapple.
    Price - 25$

    Bruschetta:
    Moazzarella cheese and diced Roma tomatoes
    marinated in olive oil, fresh garlic and basil.
    (No tomato sauce)
    Price - 22$
    '''

menu_ld = [{'Traditional': 19}, {'Margherita': 22}, {'Pizza Bianca': 21},
           {'Marinara': 17}, {'Havaiian': 25}, {'Bruschetta': 22}]

all_stuff = ['Hanna', 'Greg', 'Michael', 'Chloe', 'Tyler', 'Ashley', 'Jessica']
stuff = random.choice(all_stuff)

greetings = ['Hi!', 'Hello!', 'Yo!', 'Sup?', 'Whazzup?', 'Howdy!', 'Hi there!']
hi = random.choice(greetings)

misunderstanding = [
    'What do you mean? Does it mean yes or no?',
    'Could you please repeat that?',
    'Sorry, I dont understand. Do you mean yes?',
    'Not so fast cowboy! You push a wrong button ~_~',
    'C\'mon dude! Do you want some pizza or not?'
]


# CHAT STARTS HERE>>>>

print("********************************************")
print('''
{} My name is {}! What do I call you?
'''.format(hi, stuff))
usr_name = input()

print('''
Nice to meet you, {}! Looking for some classic italian pizza? [Y/n]:
'''.format(usr_name))

while True:
    response = input().upper()

    if re.match("[Y]", response):
        print()
        break
    elif re.match("[N]", response):
        print()
        print("Ok {}. See you later!".format(usr_name))
        exit()
    else:
        print()
        print(random.choice(misunderstanding))
        print()

print("Here is our short menu:")
print()

with open('pizza.json') as f:
    short_menu = json.load(f)
for pizzas in short_menu:
    print(pizzas['position'], pizzas['name'])

print()
print('''
Choose what do you like and press its number. Just one number of one pizza ^_^
If you want more then one... Keep calm and choose your FIRST pizza '_'
If you want to see our Full Menu with prices just type "Menu"
When you choose enough of pizza type "Done"
''')

basket = []


while True:
    usrs_choice = input()

    if re.match("[M,m]", usrs_choice):
        print(menu_full)
        continue

    elif re.match("[D,d]", usrs_choice):
        print("Ok dude! I need to write more python code to serve you")
        break

    elif re.match("[1,2,3,4,5,6]", usrs_choice):
        for pizdict in short_menu:
            if int(usrs_choice) == pizdict['position']:
                flag = True
                for u_o in basket:
                    if u_o['name'] == pizdict['name']:
                        u_o['quantity'] += 1
                        flag = False
                if flag is not False:
                    basket.append({'name': pizdict['name'], 'quantity': 1})

    else:
        print()
        print(random.choice(misunderstanding))
        print()

else:
    print('Wrong input')

print(basket)
