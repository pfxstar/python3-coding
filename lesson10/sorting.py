def bubble_sort(n):
    for i in range(0, len(n)):
        for j in range(0, i):
            if n[j] > n[j + 1]:
                c = n[j]
                n[j] = n[j + 1]
                n[j + 1] = c
    return n

#ns = Number String
ns = input("Please input a string of numbers, split by commas: ")
n0 = [int(n) for n in ns.split(",")]
n1 = bubble_sort(n0)
print(n1)