''' def bubble_sort(n):
    for i in range(0, len(n)):
        for j in range(0, i):
            if n[j] > n[j + 1]:
                c = n[j]
                n[j] = n[j + 1]
                n[j + 1] = c
    return n '''

def bubble_sort(arr):
    for j in range(0, len(arr)):
        for i in range(0, len(arr) - j - 1):        
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr

# ns = Number String
''' ns = input("Please input a string of numbers, split by commas: ")
n0 = [int(n) for n in ns.split(",")]
# n1 = bubble_sort([5, 6, 2, 100, 234, 1])
n1 = bubble_sort(n0)
print(n1) '''