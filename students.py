from seal import fibonacci, sorting
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

# Python Random Module
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
print(math.fabs(-134))