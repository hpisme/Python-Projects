"""Printing"""

print("Hello, World!")
print('Hello, World!')

"""Variables"""

#Be careful about naming variables. Make sure the name makes sense.
my_variable = 'Hello' #Assigning a string to a variable
other_variable = 123 #Assigning a number to a variable
this_variable = 3.5 #Assigning a float to a variable

"""Strings"""

#Multi-line strings
a = """Hello,
this is a multi-line string"""

#Accessing elements in a string
print('Hello'[0]) #Will print "H"

#Can iterate through strings
for x in 'Hello':
  print(x)
  
#String functions include the len function which returns the length of a string
print(len('Hello'))

#Strings can be sliced
print('Hello'[:3])

#Strings can be concatenated
#But an error will be produced when trying to concatenate different data types
print('Hello!' + ' John')
print('Hello!' + 123) #Will produce an error
