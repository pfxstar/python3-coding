students = ["Abella", "Alex", "Sophia", "Felix", "George", "Lily"]
scores = [100, 99, 75, 0, 80, 98]
print(students[2])
print(scores[2])
print(scores[5])
print(scores[-1])
for i in range(0, 5):
    print(str(i) + ": " + students[i])
index = int(input("Input number from 0 - 5 "))
print(students[index])
print(scores[index])
print(students[1:5])
print(students)
print(students[1:])
scores[1] = 1
print(scores)