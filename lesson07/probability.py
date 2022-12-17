def stupoo(a, b):
    total = b
    for i in range (a - 1):
        total = total * b
    return total

a = int(input("Please input plate number "))
b = int(input("Please input types of food "))
print(stupoo(a, b))

c = int(input("Please input number of digits "))
d = int(input("Please input numbers you can use "))
print(stupoo(c, d))