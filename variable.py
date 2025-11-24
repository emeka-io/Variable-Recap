# Printing Variables
s = 'say'
j = 'bake'
k = 'call'
print(s, j, k) # this prints all the variables in one line

# Taking Multiple Input in Python
# takimg 2 inputs using 'split()'
x, y = input('Enter two numbers: ').split()
print(f'Number of tables: {x}')
print(f'Number of chairs: {y}')
print("are you ok?")

# takimg 3 inputs using 'split()'
a, b, c = input("Enter three numbers: ").split()
print(f'Numbers of books: {a}')
print(f'Number of pens: {b}')
print(f"Number of Pencils: {c}")

# Finding DataType of Input in Python
print(type(a))
print(type(name))

# Python Variables
# assigning values
a = 'apple'
b = 25
#Assigning the Same Value to multiple variables
r = e = d = j = 50
#Assigning the Different Value to multiple variables
r, e, d, j = 3, 5, 'life', 8.05

# Type Casting a Variable
# using int()
num = 56.05
print(int(num)) # this converts it to an integer
# using float()
numb = 67 
print(float(numb))
# using str()
number = 43
print(str(number))

# Object Reference in Python
j = 5
k = j
j = 20
print(j, k) # note that k still = 5

# Delete a Variable Using del Keyword
i = 50 
del i # this deletes i from the program

# Swapping Two Variables
d = 10
w = 40
d, w = w, d
print (d, w)

# Counting Characters in a String
name = 'EMEKA'
length = len(name)
print(f'Length of the word: {length}')
