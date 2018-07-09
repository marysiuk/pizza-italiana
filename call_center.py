"""Pizza call-center.

Menu of pizza was taken from:
http://www.johnspizzerianyc.com/Times-Square-Menu/Pizza

"""
import random
# import re

menu_full = '''
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

print('''
{} My name is {}! What do I call you?
'''.format(hi, stuff))
usr_name = input()

print('''
Ok {}! Looking for some classic italian pizza?
Check it out:'''.format(usr_name))

# Need 'Yes_or_No' question here with RE (regular expressions) use.

print(menu_full)
