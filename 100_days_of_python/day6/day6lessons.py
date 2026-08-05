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
