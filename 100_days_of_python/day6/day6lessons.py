#DAY6 - Lesson 1 - Functions
''
A function in its simplest form is just a wrapper name for a block of code.
You give it name and then when you call the function by that name,
all the code within the function block will be executed.
It can help us save time and reduce repeated code.
'''

''' Defining a new Function 
def <function name>():
    print("Hello")
    # Do something else
    # Do something else ...
'''


def my_function():
        print("Hello")
        print("Bye")

my_function()

#   Reeborg challenge - Make the robot turn right
# URL -> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
'''

#   Reeborg challenge - hurdle 1
#   My solution
''' 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
x = 1
while x < 13:
    if wall_in_front() == True:
        jump()
        x += 1
    else: 
        move()
        x += 1
'''

#   Teachers solution
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
'''

#DAY6 - INDENTATION
'''
def my_function():
[indent]print("Hello")
print("Hello") # Not included in the function


def my_function2():
[indent]if sky == "clear":      
[indent][indent]print("blue")   #2x indent, 1st for the function, 2nd to make it be in the if block
[indent]elif sky == "cloudy":
[indent][indent]print("grey")
[indent]print("hello")
print("World")
'''

#       Spaces vs Tabs
''' --> URL: python.org/dev/peps/pep-0008/#tabs-or-spaces
        python.org states spaces are the preferred indentation method.
        Tabs should be used solely to remain consistent with code that is already indented with tabs.
        ! Python 3 disallows mixing the use of tabs and spaces for indentation
        ! Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.            
                        
--->    URL: official python style guide: https://peps.python.org/pep-0008/
'''

#DAY6: While loop
'''
        Syntax:
        while something_is_true:
        # Do something
        # Then do something else
'''
# URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
'''
#       Teachers example Reeborg hurdle 1 with while-loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
'''

#       Reeborg - Hurdle 2 challenge
#       My solution:
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:       # <--- This was the solution i did, eg. changed the while loop condition
    jump()
'''
#       Teachers solution (compare readability of while statement)
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
'''

#       When to use a for loop   -> when to iterate through something eg. a list
#                                -> or using a known range
#                                -> or a sequence based task
#       When to use a while loop -> Warning infinite loop possible;
#                                -> Unknown iteration count
#                                -> Waiting for an event
#                                -> Creating game loops.

#DAY6 - Reeborg - Challenge hurdle 3
#       URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#       My Solution
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() == False:
        jump()
    else:
        move()
'''

#       Teachers solution
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# ! --> Notice how teachers example checks for wall in front -> cleaner 
#       since if-statements evaluates and resolves if condition is true
while not at_goal():
    if wall_is_front(): 
        jump()
    else:
        move()
'''
