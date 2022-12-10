def find_remainder(stu, bx, sx):
    return bx * 8 + sx * 3 - stu    



"""stu = int(input("input people number "))
bx = int(input("input big box number "))
sx = int(input("input small box number "))
re = find_remainder(stu, bx, sx)
print(re)"""

run = True
while run:
    stupoo = int(input("input stupoo number "))
    
    if stupoo < 0:
        run = False
        break

    stupee = stupoo % 3
    if stupee == 1:
        print("your donut is choco dip ")
    elif stupee == 2:
        print("your donut is vanilla dip ")
    else:
        print("your donut is honey dip ")