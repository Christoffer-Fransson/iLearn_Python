#DAY8: LESSON 1 - Functions with inputs
'''
def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
'''



#   Creating the function
def greet(test_name):
    print(f"Hey! {input}")
    print("print statement 2")
    print("print statement 3")

#   Using the function
greet("Tommy")


# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello! {name}")
    print(f"How do you do {name}")

greet_with_name("Billie")
greet_with_name("Tommy")

# ! -->   Parameter is what the function ingoing variable is called
# ! -->   Argument: Is what the value of the parameter is called

#	Lesson 3 - Coding Exercise: Life in Weeks
def life_in_weeks(current_age):
    total_weeks = 90 * 52
    current_weeks = current_age * 52
    remaining_weeks = total_weeks - current_weeks

    print(f'You have {remaining_weeks} weeks left.')

life_in_weeks(20)



#   LESSON 4 - Positional VS Keyword Arguments
# Functions with mor than 1 input
def greet_with(name,location):
    print(f'Hello! {name}!')
    print(f'What is it like in {location}?')

greet_with("Jack Bauer", "Nowhere")

#   POSITIONAL ARGUMENTS
#   It takes the position of the data, checks both arguments and the first argument gets assigned to the first parameter, the second argument to the 2nd parameter.
#   This is called positional argument in python eg: parameter is matched positionally
greet_with("Nowhere", "Jack Bauer")

# KEYWORD ARGUMENTS
# we can add named parameters eg. name = "JAck Bauer", location = "Nowhere" this way the position is irrelevant as in positional arguments.
print("Keyword Arguments")
greet_with(location = "Nowhere", name = "Jack Bauer Jr")

#   LESSON 5 - CODING EXERCISE - Love Calculator
def calculate_love_score(name_a, name_b):
    both_names = name_a + name_b

    true = 0
    love = 0
    for letter in both_names:
        if letter.upper() in "TRUE":
            true += 1
        if letter.upper() in "LOVE":
            love += 1

    print(f'{true}{love}')


calculate_love_score("Angela Yu", "Jack Bauer")    

#	LESSON 6 - CEASER CYUPER - Part 1 Encryption

