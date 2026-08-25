# DAY10: Lesson 1 -  Functions with Outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name("AnGeLa", "YU"))



# difference between using print and functions
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))
print(output)


# DAY10: Lesson 2 - Multiple Return Values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("This got printed")   # will not be printed because it is not included in the return

print(format_name(input("What is your first name? "), input("what is your last name? ")))
# LEAP YEAR TEST - pass
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False     



# DAY10: Lesson 3 - Docstrings

def name_of_function(parameter):
    """Doc Strings goes here and provides mouseover information about the function"""  # !!! NOTE: No spaces after or in front of """
    print("hello")

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



name_of_function("test")    # hover over the function call to see Doc string infor at bottom
format_name("test")         # hover over the function call to see Doc string infor at bottom


# IT IS PYTHONIC NOT TO USE MULTI LINE COMENTS SIMILIAR TO SQL USING DOC STRINGS
# USE REGULAR BY LINE COMMENTING
# FOR EACH LINE INSTEAD -> CTRL + / SHORTKEY


#DAY10: Calculator project
# My solution (not optimised but works note: no while loop exit in task)
import art
def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary. Keys = "+", "-", "*", "/

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations - Multiply 4 * 8 using the dictionary
# result = operations["*"](4,8)
# print(result)

# TODO: Finish the program

def calc_engine(n1, operator, n2):
    calculation_result = operations[operator](n1, n2)
    return calculation_result

continue_run = True
print(art.logo)
nr1 = int(input("What's the first number: "))
while continue_run:
        operator = str(input("+\n-\n*\n/\nPick an operation: "))
        nr2 = int(input("What's the next number: "))
        result = calc_engine(nr1, operator, nr2)
        print(f"{nr1} {operator} {nr2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ")

        if choice.lower() == 'y':
            nr1 = result
            operator = str(input("+\n-\n*\n/\nPick an operation: "))
            nr2 = int(input("What's the next number: "))
            result = calc_engine(nr1, operator, nr2)
            print(f"{nr1} {operator} {nr2} = {result}")
            choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ")

        if choice.lower() =='n':
            print("\n" * 100)
            print(art.logo)
            nr1 = int(input("What's the first number: "))
            operator = str(input("+\n-\n*\n/\nPick an operation: "))
            nr2 = int(input("What's the next number: "))
            result = calc_engine(nr1, operator, nr2)
            print(f"{nr1} {operator} {nr2} = {result}")
            choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ")


# Teachers solution
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input("Type 'y' to continue calculate with {answer}, or type 'n' to start a new calculation. ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()
