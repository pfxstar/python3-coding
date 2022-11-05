import random

print("Hello!")
name = input("What is your name? ")
print("Hello, " + name + ".")
gender = input("What is your gender? (m(Male) or f(Female)) ")
gender.lower()
if gender == "m":
    gender = "male"
else:
    gender = "female"
f_guide = ["Sarah", "Ellie", "Ayla", "Eileen", "Helen"]
m_guide = ["Chris", "Ryan", "Cameron", "Ethan", "Gordon"]
guide_name = "name"
index = random.randint(0, 4)
if gender == "male":
    guide_name = m_guide[index]
else:
    guide_name = f_guide[index]
print("My name is " + guide_name + ".")
print("Well, " + name + ", I have to show the basics first.")
print("When you can type something (input), please input asked options or if it is a freestyle one, you can write anything you want by as long sa it corre-sponds to the question.")
print("Now I'll quiz you freestyle questions to know your preference.")
fav_animal = input("What is your favorite animal? ")
fav_food = input("What is your favorite food? ")
hobby = input("What is you hobby? ")
fav_drink = input("What is your favorite drink? ")
fav_game = input("What is your favorite game? ")
print("Okay! Let's start. I'll introduce you to your home. ")
pet = "no"
print("Hm... This place really needs a glow-up. To the shop!")
print("Loading...")
pet = input("Do you want a pet?(yes or no)")
pet.lower()