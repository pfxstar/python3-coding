import random

"""
print("*    *".center(10));
print(" * * " * 2)
print("*   *" * 2)
print(" *" + " " * 6 + "* ")
print("  *  " * 2)
print("   * " + " *  ")
print("    *" + "*   ")
"""
print("   ❤ ❤ ❤   ❤ ❤ ❤")
print(" ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤")
print("❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤")
print(" ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤")
print("   ❤ ❤ ❤ ❤ ❤ ❤ ❤")
print("     ❤ ❤ ❤ ❤ ❤")
print("        ❤ ❤")
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
index = random.randint(0, 5)
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
fav_place = input("What is your place? ")
print("Okay! Let's start. I'll introduce you to your home. ")
pet = "no"
print("Hm... This place really needs a glow-up. To the shop!")
print("Loading...")
pet = input("Do you want a pet? (yes or no) ")
pet.lower()
if pet == "yes":
    pet_type = input("What type of pet do you want? ")
    print("Let's add that...")
else:
    print("Okay!")
print("Hm... I'm really hungry. Why don't we go eat " + fav_food + "?")
print("Loading...")
print("This is really good!")
print("Eating...")
print("Hm... I really bored. Let's play a game! It's called 'Who am I?' ")
whoami1 = input("I am small, clear and I am always different. Who am I?")