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
print("Well," + name + ", I have to show the basics first.")
print("When you can type something (input), please input asked options or if it is a freestyle one, you can write anything you want by as long sa it corre-sponds to the question.")