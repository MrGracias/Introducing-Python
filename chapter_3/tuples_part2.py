'''
ogracias
Current Module: chapter_3.tuples
'''
#===============================================================================
# Tuples are immutable, unlike lists.
# tuples are sort of a CONSTANT list
#===============================================================================
from ntpath import sep

empty_tuple = ()
print(empty_tuple)

# Follow each tuple with a comma
one_marx = ('Groucho',)
print(one_marx)

#===============================================================================
# Tuple UNPACKING (assigning variables to each element)
#===============================================================================
# You can assign multiple variables at once with a tuple
marx_tuple = ('Groucho', 'Chico', 'Harpo')
x, y, z = marx_tuple
print(x, y, z)

# You can exchange values w/o temp values
password = 'swordfish'
ice_cream = 'strawberry'
print('password:', password)
print('ice_cream:', ice_cream, '\n\n')

# Exchange the values
password, ice_cream = ice_cream, password
print('password:', password)
print('ice_cream:', ice_cream,'\n\n')

#===============================================================================
# Convert into a tuple
#===============================================================================

marx_list = ['Groucho', 'Chico', 'Harpo']
print(marx_list)
marx_new_tuple = tuple(marx_list)
print(marx_new_tuple)


print('Why tuples?')
#===============================================================================
# Use less space
# You can't clobber them by mistake
# You can use tuples as dictionary keys
# Named tuples can be an alternative to objects
# Function arguments are passed as tuples
#===============================================================================

