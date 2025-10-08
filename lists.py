users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Matthew'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

# Add but don't replace in list
users[2:2] = ['Eddie', 'Alex']
print(users)

# Replace members of list at specified place
users[1:3] = ['Robert', 'JP']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['matthew']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

print("")

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)
print("")
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

print("")

# Assigning values in a tuple to new variables
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

print("")
