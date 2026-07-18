print("Hello World")
print('Hello')

# Assign String to a Variable
name = "Python"
print(name)
# Type  a Value
print(type(name)) #String

# String to Array
print(name[0])
print(name[3])

# String Length
name = "Python Development"
print (name)
print (len(name))

# String Slicing
# SYNTAX
# [Startindex : EndIndex]
print(name)
print(name[0:18])
print(name[0:])
print(name[ :18])
print(name[3:8])
print(name[3: ])

# Negetive Indexing
print(name[-6:-1])

# Multiline String
a = """" Hello Tanvi
How Are you,
I Am Fine,
Thanku;"""
print(a)

# Looping Through a String
# loop to a line to line

for x in "python":
 print (x)

for a in "Tanvi":
  print(a)

# Assign String to a Variable
a = "python"
for x in a: #  a to len this time to print a value / python to 6 time
  print(a)

# Check String
name = "Hello World"
print("d" in name) # True / False

# Python - Modify Strings
# Upper case
a = "hello world"
print(a.upper())

# Lower Case
a = "HELLO WORLD"
print(a.lower())

# Remove Whitespace
a = "HELLO WORLD"
print(a.strip())

# Replace String
a = "HELLO WORLD"
print(a.replace("H", "o"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concat a String
name = "Sliver oak University "
city = "Ahmedabad "
print(name + city)
print(city + name)
