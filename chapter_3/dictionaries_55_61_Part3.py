'''
ogracias
Current Module: chapter_3.dictionaries_55_61_Part3
'''
empty_dict = {}
print(empty_dict, '\n\n')

bierce = {'day': ' A period of 24 hours, mostly spent',
          'positive': 'Mistaken at the top of one\'s voice',
          'misfortune': 'The kind of fortune that never misses'
          }
print('bierce:', bierce, '\n\n')


#===============================================================================
# Convert into dict from lists, tuples, and strings
#===============================================================================
print('from lists to dictionary')

# 1) Dictionaries use the key:value system.
# Let's make a dict from a number of lists
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print('lol list:', lol)
my_dictionary = dict(lol)
print('my_dictionary:', my_dictionary, '\n\n')

print('from tuples to dictionary')
# 2) Dictionaries use the key:value system.
# Let's make a dict from a number of tuples
# from within a list structure.
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print('lot list:', lot)
my_dictionary_fromTuple =  dict(lot)
print('dict from tuple:', my_dictionary_fromTuple, '\n\n')



print('from a list of 2-char strings')
los = ['ab', 'cd', 'ef']
print('los:', los)
from_2_char_string = dict(los)
print('from_2_char_string:', from_2_char_string, '\n\n')

#===============================================================================
# Adding an item to a dict
#===============================================================================
pythons = {'Chapman': 'Graham',
           'Cleese' : 'John',
           'Idle' : 'Eric',
           'Jones' : 'Terry',
           'Palin': 'Michael'
           }

print('pythons:', pythons, '\n\n')

# let's add another member to the dict
pythons['Gillian'] = 'Gerry'
print('After adding 1 more item', pythons)

# Let's correct it from Gerry to Terry
pythons['Gillian'] = 'Terry'
print('After correcting Gerry:', pythons, '\n\n')


some_pythons = {'Graham': 'Chapman',
           'John' : 'Cleese',
           'Eric' : 'Idle',
           'Terry' : 'Gillian',
           'Michael': 'Palin',
           'Terry' : 'Jones'
           }
# It only prints the last value for Terry = (Jones)
print('some_pythons:', some_pythons)

#===============================================================================
# Combine dictionaries with update()
#===============================================================================
others = {'Marx': 'Groucho', 'Howard' : 'Moe'}

# Let's combine them:
some_pythons.update(others)
print('Combined dicts: ', some_pythons)

print('\n\n')

print('''
#===============================================================================
# What happens if second dict has same key as original?
#===============================================================================
''')
first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}

first.update(second)
print('first:', first)

print('''
#===============================================================================
# delete an item with del
#===============================================================================
''')

print('some_pythons:', some_pythons)

# Let's delete the last 2 entries:
del some_pythons['Howard']
del some_pythons['Marx']
print('some_pythons:', some_pythons)

print('''
#===============================================================================
# Delete all items by using clear()
#===============================================================================
''')
some_pythons.clear()
print('some_pythons:', some_pythons)

print('''
#===============================================================================
# test for a key by using: in
#===============================================================================
''')
colors = {'rojo' : 'red', 'azul' : 'blue', 'negro' : 'black'}
print('colors:', colors)

rojo_in_colors = 'rojo' in colors
print('Is there rojo in colors?', rojo_in_colors)

isGillianThere = 'Gillian' in colors
print('isGillianThere:', isGillianThere)


print('''
#===============================================================================
# get an item by key, and exception when not
# found
#===============================================================================
''')
# Uncomment below, you will get an error, since
# Gillian is not found in colors.

# rojo = colors['Gillian']
# print(rojo)

# To avoid this:
rojo = colors['rojo']
print(rojo)

print('''
#===============================================================================
# Avoid exception using get(): You will get NONE
#===============================================================================
''')
rojo = colors.get('Gillian')
print('rojo:', rojo)

# give an alternative message when not found
rojo = colors.get('Gillian', 'Key not found!')
print('rojo:', rojo)

print('''
#===============================================================================
# get all keys using keys() [Use list() to make into list
#===============================================================================
''')
signals = {'green': 'go',
           'yellow' : 'go faster',
           'red' : 'smile for the camera'
           }
print('keys for signals:', signals.keys())

# You may want these keys in a list instead of a string
print('list of keys:', list(signals.keys()))


print('''
#===============================================================================
# Get all values using values()
#===============================================================================
''')
print(list(signals.values()))

print('''
#===============================================================================
# get all key-value pairs using items()
#===============================================================================
''')
print(list(signals.items()))

print('''
#===============================================================================
# Assign with =, copy with copy()
#===============================================================================
''')
print('signals:', signals)
save_signals = signals
save_signals['blue'] =  'confused'
print('signals:', signals, '\n\n')
# All changes are reflected on any name
# referring to same address.

copied_signals = signals.copy()
signals['Gray'] = 'grey_value'
print('copied_signals:', copied_signals)
print('signals:', signals)

