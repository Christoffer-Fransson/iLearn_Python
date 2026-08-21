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

