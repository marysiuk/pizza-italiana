"""Pizza call-center.

Menu of pizza was taken from:
http://www.johnspizzerianyc.com/Times-Square-Menu/Pizza

"""

# HERE IS THE CONTENT THAT WE GONNA USE>>>>

import random
import re
import json

with open('pizza.json') as f:
    short_menu = json.load(f)


# ******************** Here is block of chat texts:
stars = "********************************************"


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


all_stuff = ['Hanna', 'Greg', 'Michael', 'Chloe', 'Tyler', 'Ashley', 'Jessica']
stuff = random.choice(all_stuff)


greetings = ['Hi!', 'Hello!', 'Yo!', 'Sup?', 'Whazzup?', 'Howdy!', 'Hi there!']
hi = random.choice(greetings)
welcome = ('''
{} My name is {}! What do I call you?
''')
ntmy = ('''
Nice to meet you, {}! Looking for some classic italian pizza? [Y/n]:
''')  # ntmy means "nice to meet you" :)


misunderstanding = [
    '\nWhat do you mean? Does it mean yes or no?\n',
    '\nCould you please repeat that?\n',
    '\nSorry, I dont understand. Do you mean yes?\n',
    '\nNot so fast cowboy! You push a wrong button ~_~\n',
    '\nC\'mon dude! Do you want some pizza or not?\n'
]


instructions = ('''
If you want to see our Full Menu with prices just type "Menu"
Choose what do you like and press its number. Just one number of one pizza ^_^
If you want more then one... Keep calm and choose your FIRST pizza '_'
When you choose enough of pizza type "Done"
    ''')


# ******************** CHAT STARTS HERE>>>>


print(stars)
print(welcome.format(hi, stuff))
usr_name = input()

print(ntmy.format(usr_name))

while True:
    response = input().upper()

    if re.match("[Y]", response):
        print()
        break
    elif re.match("[N]", response):
        print("\nOk {}. See you later!\n".format(usr_name))
        exit()
    else:
        print(random.choice(misunderstanding))


print(stars)
print("\nCool! Here is our short menu:\n")

for pizzas in short_menu:
    print(pizzas['position'], pizzas['name'])

print(instructions)


basket = []


while True:
    usrs_choice = input()

    if re.match("[M,m]", usrs_choice):
        print(menu_full)
        continue

    elif re.match("[D,d]", usrs_choice):
        print("\nWell! I need to write more python code to serve you\n")
        break

# *** "pizdict" isn't what it looks like, particulary for the Russian-speaking!
# It's short for "Pizza Dictionary" ^_^
    elif re.match("[\d]", usrs_choice):
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
        print(random.choice(misunderstanding))

print(basket)  # This print() is just to see how this stuff works.
