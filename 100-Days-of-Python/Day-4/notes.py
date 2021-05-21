"""Lists"""

#Lists are ordered, changeable, and allow duplicates. 
#Lists can be created with square brackets
#Lists can have different data types

this_list = ['String', 3.5, 2, True]
print(this_list)

#Strings can be sliced
print(this_list[:2])

#Strings can be iterated through
for x in this_list:
  print(x)
  
#List items are indexed. Indexing starts at 0.
print(this_list[2])

#You can also find a negative index
print(this_list[-1])

#Adding to a list using append
this_list.append('Added')

#Replacing items at a specific index
this_list[0] = 'String2'

#Lists can be nested
this_list_2 = [['Apple', 'Orange', 'Pear'], 123, True]

