'''
ogracias
Current Module: Indexes and slicing
'''
letters = 'abcdefghijklmnopqrstuvwxyz'

print('Print first element:')
print(letters[0])

print('Print last element:')
print(letters[-1])


print()
print('****************** Slicing ******************')
print() 
print('All letters:', letters[:], '\n')

print('from 20th on:', letters[20:], '\n')

print('Last 3 characters:', letters[-3:], '\n')

print('from 6th to 3rd from the end:', letters[-6:-2], '\n')

print('Backwards:', letters[-1::-1], '\n')

print('from 10th backwards:', letters[9::-1], '\n')

#Alternative way to print backwards
print('Backwards:', letters[::-1], '\n')

#You can also go beyond the specific range
print('from a higher index #:', letters[50::-1], '\n')

#also out of range
print('from lower index #:', letters[-50:50], '\n')

#for a range with no elements and out of range
print('Out of range index #:', letters[70:72], '\n')







