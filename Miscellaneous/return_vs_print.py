# Lesson 3.03 return vs print

import random
# inputs:  x (int), y (int)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y

def mystery_function(x, y):
    random_number = random.randint(-4, 4)
    print(random_number)
    if random_number > 0:
        z = x + y
        return z
    else:
        z = x * y
        return z


if __name__ == '__main__':
    print(mystery_function(1, 2))
    