id = {1, 2, 3, 4, 5, 6}
id_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
mixed_id = {'1', 2, 3.0, '4', 5, 6.0}

print(id)
print(mixed_id)

# Creating an empty set
empty_set = set()

# This is creating an empty dictionary
empty_dict = {}

# The types of empty_set & empty_dict
print(type(empty_set))
print(type(empty_dict))

# Creating a duplicate item in a set
duplicate_set = {1, 1, 2, 3, 4, 5, 6}

print(duplicate_set) # It ignores the duplicate value

# Adding items in sets
print(empty_set) # This is an empty set

empty_set.add(50)
print(empty_set)

# Joining two collection types together (The duplicates are removed)
set_1 = {50, 80, 90}
set_2 = {50, 70, 10}
set_1.update(set_2)
print(set_1)

tup_1 = ('a', 'b', 'c')
set_1.update(tup_1)
print(set_1)

list_1 = [5, 10, 'Hello']
set_1.update(list_1)
print(set_1)

dict_1 = {'LA': 5, 'LO': 10, 'LE': 'Bye'}
set_1.update(dict_1)
print(set_1)

# Removing items from a set
removed = set_1.discard('5')

print(set_1)
print(removed) # This returns None

# The all() function
print(all(set_1))

# The any() function
print(any(set_1)) # If one is True, returns True

# Using sets in for loops
for value in set_1:
    print(value)

for index, value in enumerate(set_1):
    print(index, end = ', ') # The enumerate() function adds a counter to the set
    print(value)

# The len() function
print(len(set_1))

# min(), max(), and sum()
'''
print(max(set_1)) # Only same datatypes can be compared

print(min(set_1)) # Only same datatypes can be compared

# print(sum(set_1)) # Only numbers can be summed together
'''

# The sorted() function

set_3 = {1, 3, 4, 2, 6, 5}
sorted_set = sorted(set_3)
print(sorted_set)
print(set_3)

'''
sorted_set = sorted(set_1)
print(sorted_set)
''' # This code raises an error; only same datatypes can be sorted

# Checking if a value exists in a set
print(6 in set_3) # True
print(10 in set_3) # False

# Union of two sets
A = {1, 3, 5}
B = {2, 4, 6}

# Method 1: |
print(A | B)

# Method 2: union()
print(A.union(B))

# Intersection of two sets
C = {1, 2, 3}

# Method 1: &
print(A & C)

# Method 2: intersection()
print(A.intersection(C))

# Difference of two sets

# Method 1: -
print(A - C)

# Method 2: difference()
print(A.difference(C))

# Symmetric different of two sets

# Method 1: ^
print(A ^ C)

# Method 2: symmetric_difference()
print(A.symmetric_difference(C))

if A == B:
    print('Equal')
else:
    print('Not Equal')