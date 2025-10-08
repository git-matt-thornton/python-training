import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")  # defaults to read
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist.\n")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt", "r")
print(f.read())
f.close()

# Write overwrites
f = open("context.txt", "w")
f.write("I deleted all of the context.\n")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist

f = open("list_of_names.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
    print("Created dave.txt\n")

# Delete a file
# Avoid an error if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
    print("Deleted dave.txt.\n")
else:
    print("The file you wished to delete does not exist.\n")

with open("more_names.txt", "r") as f:
    content = f.read()
    f.close()

with open("names.txt", "w") as f:
    f.write(content)
    f.close()
