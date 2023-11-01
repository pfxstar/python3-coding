'''
file1 = open("C:/Users/abell/Downloads/MyStoryBook.txt", "r")

content = file1.read()
print(content)

file1.close()

try:
    file1 = open("Hello, World!")
    read_content = file1.read()
    print(read_content)
except:
    print("There is no such file. Please rewrite your memory.")
finally:
    file1.close()
'''

with open("C:/Users/abell/Downloads/MyStoryBook.txt", "r+") as file2:
    content2 = file2.read()
    file2.write(" The character was called Lily.")
    content3 = file2.read()
    print(content2)
    print(content3)

    