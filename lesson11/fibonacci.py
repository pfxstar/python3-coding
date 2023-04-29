def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)

def better_fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    pre = 0
    cur = 1
    nxt = 0
    count = 1
    while count < n:
        nxt = pre + cur
        pre = cur
        cur = nxt
        count += 1
    return nxt

while True:
    n = int(input("Input a number ( Press Ctrl + C to quit :,( ) "))
    print(better_fibonnaci(n))