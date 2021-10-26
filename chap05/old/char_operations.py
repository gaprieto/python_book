# char_operations.py
# Basic character string operations

a = "Hello World!"
b = "Python"

c = a[0:6] + b # concatenation
print(c)

c = b*2 # Repetition
print(c)

print(a[:5],a[6:]) # Range Slice

# Find characters
i = a.find("ello")
print (i)

# Remove blanks
c = "   "+a+b+"  "
print(c)
d = c.strip()
print(d)

# Split string, with whitespace delimiter
c = a.split()
print(c)


