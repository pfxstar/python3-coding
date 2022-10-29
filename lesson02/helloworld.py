import random

print("Hello World!")
name = input("What is your name? ")
print("Hello, " + name + ".")
guide_names = ["Bonnie", "Carm", "Ella", "Derick"]
# print(guide_names[2])
index = random.randint(0, 4)
# print(index)
print("My name is " + guide_names[index] + ".")
place = input("Where do you want to go? ")
print("Going to " + place + "...")
print("It is so fun here!")
print("I think we should go eat!")
eat = input("McDonald's or KFC? ")