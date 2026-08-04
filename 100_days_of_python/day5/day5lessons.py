#DAY5: LESSON 1 - For Loops
'''
Syntax
for <variable name of each item> in <a List>:
    <do something>
    <do something else>
'''

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")

# ---> INDENTATION IS IMPORTANT IN PYTHON PROGRAMMING.
'''
Every time you see the : symbol used, you need to be careful about the indentation that comes afterwards.

e.g. This code will behave very differently

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
from this code:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")
'''

