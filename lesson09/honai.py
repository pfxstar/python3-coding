step = 0

# Recursive Function: A function that calls itself
def hanoi(n, start, temp, end, step):
    # Condition to end recursive function
    if n == 1:
        step += 1
        print(step, start + " --> " + end)
        return
    
    hanoi(n - 1, start, end, temp, step)
    hanoi(1, start, temp, end, step)
    hanoi(n - 1, temp, start, end, step)
    
n = int(input("Please input number of discs: "))
start = input("What pole is the starting pole? ")
temp = input("What pole is the assisting pole? ")
end = input("What pole is the ending pole? ")
hanoi(n, start, temp, end, step)