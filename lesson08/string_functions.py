# .lower()
a = "GO AWAY!"
# Doesn't change orginal value; Returns new value
print(a.lower())
print(a)

# .upper()
b = "hello, everyone!"
print(b.upper())
print(b)

# Look through a string
c = "hELLo EdsajM"
for i in c:
    print(i)

# Check for uppercases and lowercases
d = ";oaihejwrhqjlekhjrewbnasdf,asdfWHELWKJHSADBNSAMM"
print(d.isupper())
print(d.islower())
e = "AIUEPOAISUDSHDKSADJGHSKADJHGSASVREREO"
print(e.isupper())
print(e.islower())
# Numbers and symbols don't count
f = "023987410238497ASEURYOWQIUERHAS"
print(f.isupper())
print(f.islower())
# If there is no letters, it is False
g = "01928374019823741726357832947832647819374"
print(g.isupper())
print(g.islower())

# Split a string to a list
h = "I am very smartie sad"
arr = h.split(" ")
print(arr)

# Join a list to a string
j = ["dog", "cat", "bird", "lizard", "giraffe", "zebra", "lion", "cheetah", "leopard", "wolf", "parakeet", "parrot", "beetle", "bobcat", "chicken", "pig", "cow", "sheep"]
k = "-".join(j)
print(k)
l = " => ".join(j)
print(l)

countries = ["Canada", "China", "Cuba"]
print(" What countries have you ever been to? ")
print(" --> ".join(countries))