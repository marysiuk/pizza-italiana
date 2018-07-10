"""Pizza call-center.

Menu of pizza was taken from:
http://www.johnspizzerianyc.com/Times-Square-Menu/Pizza

"""

# HERE IS THE CONTENT THAT WE GONNA USE>>>>

import random
import re

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

misunderstanding = [
    'What do you mean? Does it means yes or no?',
    'Could you please repeat that?',
    'Yes or No? You can answer in russian if you want...',
    'Sorry, I dont understand. Do you mean yes?',
    'Not so fast cowboy! You push the wrong button ~_~',
    'C\'mon dude! Do you want some pizza or not?'
]


# CHAT STARTS HERE>>>>

print('''
{} My name is {}! What do I call you?
'''.format(hi, stuff))
usr_name = input()

# print('''
# Ok {}! Looking for some classic italian pizza?'''.format(usr_name))

print('''
Ok {}! Looking for some classic italian pizza? [Y/n (Д/н)]:
'''.format(usr_name))

while True:
    response = input().upper()

    if re.match("[YД]", response):
        print(menu_full)
        break
    elif re.match("[NН]", response):
        print()
        print("Ok {}. See you later!".format(usr_name))
        raise SystemExit(1)
    else:
        print()
        print(random.choice(misunderstanding))
        print()

print("next question")
