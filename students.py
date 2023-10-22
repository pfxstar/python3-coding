# Imports
from seal import fibonacci, sorting, utils
from seal.math import calculus
import random
import math

my_class = {
    1:{
        'first_name': 'Aahana', 
        'last_name': 'Agrawal',
        'gender': 'f'
    }, 
    2:{
        'first_name': 'Ella', 
        'last_name': 'Assiah',
        'gender': 'f'
    },
    3:{
        'first_name': 'Aiden', 
        'last_name': 'Chen',
        'gender': 'm'
    },
    4:{
        'first_name': 'Kevin', 
        'last_name': 'Chen',
        'gender': 'm'
    },
    5:{
        'first_name': 'Erianna', 
        'last_name': 'Cheng',
        'gender': 'f'
    },
    6:{
        'first_name': 'Jayden', 
        'last_name': 'Hsieh',
        'gender': 'm'
    },
    7:{
        'first_name': 'Liam', 
        'last_name': 'Hy',
        'gender': 'm'
    },
    8:{
        'first_name': 'Grant', 
        'last_name': 'Lu',
        'gender': 'm'
    },
    9:{
        'first_name': 'Maxwell', 
        'last_name': 'Luk',
        'gender': 'm'
    },
    10:{
        'first_name': 'Abella', 
        'last_name': 'Pan',
        'gender': 'f'
    },
    11:{
        'first_name': 'Gordon', 
        'last_name': 'Peng',
        'gender': 'm'
    },
    12:{
        'first_name': 'Keshav', 
        'last_name': 'Tayal',
        'gender': 'm'
    },
    13:{
        'first_name': 'Andy', 
        'last_name': 'Tian',
        'gender': 'm'
    },
    14:{
        'first_name': 'Arianne', 
        'last_name': 'Troy',
        'gender': 'f'
    },
    15:{
        'first_name': 'Terry', 
        'last_name': 'Wang',
        'gender': 'm'
    },
    16:{
        'first_name': 'Austin', 
        'last_name': 'Wong',
        'gender': 'm'
    },
    17:{
        'first_name': 'Eric', 
        'last_name': 'Wood',
        'gender': 'm'
    },
    18:{
        'first_name': 'Yurui', 
        'last_name': 'Yao',
        'gender': 'f'
    },
}

# Testing modules
''' print(fibonacci.better_fibonnaci(6))
print(fibonacci.fibonnaci(6))
print(sorting.bubble_sort([6, 2, 1, 3, 4, 5]))
print(dir())
print(calculus.hello()) '''

''' # Python Random Module
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

print(random.randrange(10, 20))
print(random.randrange(1, 2))

print(random.choice(my_class))

random.shuffle(my_list)
print(my_list)

print(random.random())

random.seed(10)
print(random.random())
print(random.random())

# Python Mathematics
print(math.pi)

print(math.ceil(1.2))
print(math.ceil(2.5))
print(math.ceil(-5.3))
print(math.ceil(10.0))

print(math.floor(10.0))
print(math.floor(254238542452.245659))
print(math.floor(-1.3))

print(math.fabs(134))
print(math.fabs(-134)) '''

# Lists
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'a']

my_list2.remove('a')
print(my_list2)

del my_list2[1]
print(my_list2)

last = my_list2.pop()
print(my_list2)
print(last)

print(my_list2.index('f'))
print(my_list2.count('d'))
print(len(my_list2))

my_list2.sort()
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)

my_list3 = ['g', 'a', 'c', 'd', 'f', 'e', 'b']

my_list3.reverse()
print(my_list3)
my_list3.sort()
print(my_list3)

my_list4 = my_list3.copy()
print(my_list4)

my_list4.append('h')
print(my_list4)
print(my_list3)

a = 3
b = a
b = 4
print(a)

c = 'etre'
d = c
d = 'avoir'
print(c)

print(min(my_list4))
print(max(my_list4))

utils.print_list(my_list4)

print('z' in my_list4)

# List Comprehensions
my_list5 = [1, 5, 8, 3, 15, 66]

''' 
for index, value in enumerate(my_list5):
    my_list5[index] *= 2 
'''

my_list6 = [i * 2 for i in my_list5]
print(my_list6)

my_list7 = [i + 5 for i in my_list5]
print(my_list7)

my_list8 = [i + 10 for i in my_list5 if i % 2 != 0]
print(my_list8)

my_list9 = [i if i % 2 == 0 else i + 10 for i in my_list5]
print(my_list9)

my_list10 = [i if i % 2 == 0 else i * 2 for i in my_list5]
print(my_list10)