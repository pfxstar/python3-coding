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

def sorting(sc):
    i = 0
    while i < len(scores)- 1:
        if sc[i] > sc[i + 1]:
            c = sc[i]
            sc[i] = sc[i + 1]
            sc[i + 1] = c
        i = i + 1
    return sc

# print(sorting(scores))


def bubble_sort(n):
    for i in range(0, len(n)):
        for j in range(0, i):
            if n[j] > n[j + 1]:
                c = n[j]
                n[j] = n[j + 1]
                n[j + 1] = c
    return n

print(bubble_sort(scores))
