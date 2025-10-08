import math

first = "Matthew"
last = "Thornton"

print('')

# Literal assignment
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatonation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?               

I was just checking in.    
                                All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                     "
multiline = "           " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print('')

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print('')

# String index values
print(first[1])
print(first[-1])
print(first[0:-1])
print(first[0:])

# Some methods return boolean data
print(first.startswith("M"))
print(first.endswith("Z"))

print('')

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print('')

price = 80
print(type(price))

grade = 3.28
print(type(grade))

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(grade))
print(abs(grade * -1))
print(round(grade))
print(round(grade, 1))
print(math.pi)
print(math.sqrt(64))
print(math.ceil(grade))
print(math.floor(grade))

# Casting a string to a number
zip_code = "100001"
zip_value = int(zip_code)
print(type(zip_value))

# Error if you attempt to cast incorrect type
zip_value = int("London")
