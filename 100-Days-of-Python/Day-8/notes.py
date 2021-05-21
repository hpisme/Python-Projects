"""Functions Continued"""

def my_function(greeting,name):
  print(greeting + ", " + name +'!')
my_function('Hello','Heather')

#Keyword Arguments or kwargs

def my_function(greeting,name):
  print(greeting + ", " + name +'!')
my_function(greeting = 'Hello',name = 'Heather')
