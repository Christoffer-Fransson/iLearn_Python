# DAY10: Functions with Outputs - Lesson 1
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
