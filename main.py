'''' type casting
x = input("1. Number: ")
type(x)
y = input("2. Number: ")
type(y)

total = int(x) + int(y)

print(total)
'''

# --------------------------------------------------

#character arrays

name = 'hilmi'
surname = 'demir'
age = 31

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'

#print(greeting)
#print(greeting[1])
#print(len(greeting))
#print(greeting[-1])    This is for use last word of string
#print(greeting[-3])
#print(greeting[1:4])   This finds letters from index 1 to index 4
#print(greeting[1:])    This finds letters from index 1 to end
# print(greeting[1:4:2]) This finds one of every 2 letters from index 1 to index 4

# -------------------------------------------------------

# string formats

# print('My name is {} {} and ı m {} years old'.format(name, surname, age))
# print('My name is {0} {1} and ı m {2} years old'.format(name, surname, age))
# print('My name is {s} {n} and ı m {a} years old'.format(n = name, s = surname, a = age))
# print('My name is {s} {n} and ı m {a} years old'.format(n = name, s = surname, a = age))

result = 200 / 700
# print('the result is {r:1.3}'.format(r = result)) second parameter for numbers after comma

# print(f'My name is {name} {surname} and ı m {age} years old'.format(name, surname, age))




