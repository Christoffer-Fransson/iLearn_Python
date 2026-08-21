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
