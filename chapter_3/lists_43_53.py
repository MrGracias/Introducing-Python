'''
ogracias
Current Module: chapter_3.lists_43_53
'''
from ntpath import sep
empty_list = []

#adding more lists
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

# You can make an empty list with the list() function
another_empty_list = list()
print('Empty list:', another_empty_list)

print()
print('****************** convert other data types to lists ******************')
print() 
print(list('cat'))

#tuple introduction example
print('Let\'s introduce a tuple:')
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))
 
#Let's continue to split
birthday = '03/10/1971'
print(birthday.split('/'))

#Another more complex split() example
split_me = 'a/b//c/d///e'
print(split_me.split('/'))

#Change the 
print(split_me.split('//'))

print()
print('****************** Getting an item by using [offset] ******************')
print() 
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[-1])
print(marxes[0])
print(marxes[0:10]) #Can include a higher index

print('an offset higher than # elements = error')
# print(marxes[5]) # Error on purpose
print(marxes[3::-1])

print()
print('****************** list of lists ******************')
print() 
small_birds  = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtle doves']
all_birds = [small_birds, extinct_birds, carol_birds]
print('all_birds:', all_birds)

# Select the first list
print(all_birds[0])

# You can print an item from a list of lists
print('Print an item in a list of lists:', all_birds[1][0])

print()
print('****************** Change an item in a list ******************')
print() 
marxes[2] = 'Wanda'
print(marxes)

print()
print('****************** Slicing a list by offset range ******************')
print() 
sliced_list = marxes[0:2]
print('sliced list:', sliced_list)

# list elements by 2
print(marxes[::2])

# list elements by -2
print(marxes[::-2])

# Reverse the order of the list
print(marxes[::-1])

print()
print('****************** Add an item at end- Append() ******************')
print() 
marxes.append('Zeppo') # append it first one by one
print(marxes)


print()
print('****************** Combine by using extend() or += ******************')
print() 

# The extend() method
new_list = ['extended1', 'extended2']
marxes.extend(new_list)
print('extend():', marxes)



# Declare others list
others = ['Gummo', 'Karl']
# Add others to marxes
marxes += others
print('+= :', marxes)

#===============================================================================
# if more than one element is appended, 
# then a new list is added as an element
#===============================================================================
last_list = [1, 2, 3] 
marxes.append(last_list)
print('append:', marxes)

print()
print('****************** insert() and delete ******************')
print() 

marxes.insert(-1 + 1, 'first') # You can also use 0
print('insert:', marxes)


#delete last item in the list ( Use the [] notation)
del marxes[-1]
print(marxes)

print()
print('****************** delete an item by value ******************')
print() 
marxes.remove('Karl')
marxes.remove('first')
print(marxes)


print()
print('****************** use pop(0) = head, tail = pop or pop(-1) ******************')
print() 
#Remove last item on the list
marxes.pop()
print('tail:', marxes)

#head
marxes.pop(0)
print('head:', marxes)

print()
print('****************** find the offset or index of an item ******************')
print() 
chico_index = marxes.index('Chico')
print('index for Chico:', chico_index)

print()
print('****************** find item in list with \'in\' ******************')
print() 
is_here = 'Zeppo' in marxes
print('Is Groucho is list?', is_here)

print()
print('****************** Going back to join() ******************')
print() 
#output is a string
print(' ::: '.join(marxes))

print()
print('****************** join() and split() ******************')
print() 
friends = ['Harry', 'Hermione', 'Ron']
print(friends)
separator = ' * '

joined = separator.join(friends)
print('joined:', joined)

# Now let's separate them
separated = joined.split(separator)
print('separated:', separated)

areBothTheSame = separated == friends
print('Are they both the same? : ', areBothTheSame)

print()
print('******************sort() and sorted() ******************')
print() 
marxes = ['Groucho', 'Chico', 'Harpo']
print('marxes:', marxes)

sorted_marxes = sorted(marxes)# Makes a copy of the list
print('sorted_marxes:', sorted_marxes)
print('marxes:', marxes, '\n\n')

marxes.sort()
print('marxes sort():', marxes, '\n\n')

#===============================================================================
# sort(): When same type, sort works correctly, even int and float,
# but when different, it may not work correctly.
#===============================================================================
numbers = [2, 1, 4.0, 3]
print('numbers:', numbers)
numbers.sort()
print('sorted numbers:', numbers,'\n\n')

# set it to descending by adding: reverse=True
numbers = [2, 1, 4.0, 3]
print('numbers:', numbers)
numbers.sort(reverse=True)
print('numbers reverse = True:', numbers)

# You can also get the length by using len
marxes = ['Groucho', 'Chico', 'Harpo']
print('len(marxes):', len(marxes))


#===============================================================================
# When assigning a list to several variables, one change
# in the list, changes it everywhere.
#===============================================================================
a = [1, 2, 3]
print('a:', a)
b = a
print('b:', b)
# Now I am going to change the first item in a
a[0] = 'surprise'
print('a:', a)
print('b:', b)

print('\n\n')
# 3 ways to copy a list 
a = [1, 2, 3]
print('a:', a)
b = a.copy()
print('b:', b)
c = list(a)
print('c:', c)
d = a[:]
print('d:', d, '\n\n')


# change only one of the elements in a.
# it shows no connection to the copies
print('a:', a)
b = a.copy()
# change the first value of a
a[0] = 'integer is changed.'
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)


