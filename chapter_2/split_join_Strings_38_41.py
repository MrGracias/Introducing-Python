'''
ogracias
Current Module: Strings
'''
from builtins import set
from lib2to3.pgen2.tokenize import tabsize
print()
print('****************** split() ******************')
print() 
todos = 'get gloves, get mask, give cat vitamins, call ambulance'
print('todos:', todos)

# Using the split() method with separator argument
split_todos = todos.split(',')
print('Using split():',split_todos)


# Using split without a separator argument
todos_NoArg = todos.split()
print('todos_NoArg:', todos_NoArg)

print()
print('****************** Combine with join() ******************')
print() 
crypto_list = ['Yetti', 'Bigfoot', 'Lock Ness Monster']
print(crypto_list)
# First the argument to join the list, and then the list to join
crypto_string = ', '.join(crypto_list)
# Use in a string
print('Found and singing book deals:', crypto_string)

#Playing with strings
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same
But that is liquid which is moist and wet
Fire that property can never get
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no double.'''

print()
print('******************  ******************')
print() 
print('First 13 characters:', poem[:13])
print('length of poem:', len(poem))
print('Does poem start with \'All\'?:', poem.startswith('All'))
print('Does poem end with \'All\'?: ', poem.endswith('All'))
word = 'the'
print('Find the word: \'the\':', poem.find('the'))
print('Find the word: \'the\' in reverse:', poem.rfind('the'))
print('Count instances of \'the\':', poem.count(word))
print('Are all characters alphanumeric?:', poem.isalnum())

print()
print('****************** Case and alignment ******************')
print() 
setup = 'a duck goes into a bar...'
print('setup string:', setup)
print('remove periods:', setup.strip('.'))
print('capitalize:', setup.capitalize())
print('title:', setup.title())
print('upper:', setup.upper())
print('lower:', setup.lower())
print('swapcase:',setup.swapcase())
print('center:', setup.center(50, '*'))
print('left justify:', setup.ljust(30, '%'))
print('right justify:', setup.rjust(30, '%'))

#Reprint the original string
print(setup)

#Substituting words
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous ', 100))

#Watch out for spaces when replacing
print(setup.replace('a', 'a famous', 100))
print('01\t012\t0123\t01234'.expandtabs(tabsize = 18))
print('Oscar\tErnesto\tGracias\tCarrillo'.expandtabs(tabsize = 18))




