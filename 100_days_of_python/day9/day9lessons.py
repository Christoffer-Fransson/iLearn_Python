#DAY9: Dictionaries, Nested Lists + Dictionaries, Blind Acution project
#   Dictionaries Lesson 1

# Syntax
'''
{key: value}
e.g.
{"bug": "An error in a program that prevents the program from running as expected."}


# To add multiple key value pairs use comma , as separator
{
"bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again.",
}
'''
# How dictionaries are written in code often.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Key can also be integer
programming_dictionary[123] = "Numbers works as keys. remember they dont need "" when calling it."
print(programming_dictionary[123])

empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)   # prints the empied dictionary

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
