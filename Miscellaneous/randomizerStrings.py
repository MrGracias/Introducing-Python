'''
Created on Jan 14, 2020
@author: ogracias
AP Computer Science Principles
Bonita Vista High
'''
import random




#random number between 1 and < 0
value = random.random()
print('Random() function:', value, '\n')

# Random floating number in a range------------------------
integerValue = random.uniform(1, 10)
print('uniform with range:', integerValue, '\n')

# You can also use the round built-in method.
# integerValue = round(random.uniform(1, 10))
# print(integerValue, '\n')



# RAndom integer in range --------
valueInt = random.randint(1, 6)
print('Random integer:', valueInt, '\n')





# toss of dice ------------------------
dice = random.randint(0, 1)
if (dice == 0):
    dice = 'heads'
else:
    dice = 'tails'
print(dice, '\n')






# from list ------------------------
greetings = ['Hello', 'Hi', 'hey', 'howdy', 'Hola']
greetSelected = random.choice(greetings)
print('One greeting selected:', greetSelected + ', Mr.  Gracias.', '\n')



#several choices ------------------------
# colors may repeat
colors = ['red', 'black', 'green', 'yellow', 'blue']
colorsChosen = random.choices(colors, k=3)
print('My 3 chosen colors are: ', colorsChosen, '\n')



#Using weights ------------------------
#38 options possible
colors1 = ['red', 'black', 'green']
colorsChosen1 = random.choices(colors1, weights=[18, 18, 2], k=3)
print('colorsChosen1 (38 possible)', colorsChosen1, '\n\n')



# random and shuffle values
# Range last parameter is NOT inclusive
deck = list(range(1, 53))
random.shuffle(deck)
print('Shuffled deck:', deck)

#FROM deck above, select 5 unique values
deck1 = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)



# actual example with making up addresses from list
# provided:
first_names = ['John', 'Jane', 'Corey', 'Travis']
last_names = ['Smith', 'Doe', 'Jenkins', 'Davis']
street_names = ['Main', 'High', 'Pearl', 'Maple']
cities = ['Metropolis', 'Eerie', 'King\'s landing', 'Sunnydale']
states = ['AL', 'CA', 'CT', 'DC']

print('\n\n')
counter = 1
for num in range(5):
    first = random.choice(first_names)
    last = random.choice(last_names)
    phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'
    street_num = random.randint(100, 999)
    streetName = random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {streetName} St. {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@gmail.com'

    print(f'{counter}: {first} {last}\
    \n{phone} \n{address}\
    \n{email}\n\n')
    counter += 1
    
