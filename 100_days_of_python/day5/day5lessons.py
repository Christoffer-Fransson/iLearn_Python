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

# DAY5: LESSON 2 - Highest score code challenge (build max() function equivalent using basic python))
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#   sum() function
#   Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)

''' But how does sum() work behind the scenes? 
    The code is written by the people who developed Python and it might look something like this '''
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score

print(f'Total sum: {sum}')
#   max() - function
''' There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers,
    and it will give you the highest number or the lowest number.'''

#   Challenge
''' Your job is to figure out how the Python programmers might have built this 
    functionality using loops and conditionals.

    You are given a list of exam scores, and you have to print out the highest score from the List. 
    You will need to use what you have learnt about Lists, For Loops and Conditionals to print out 
    the highest score in the list of student_scores. For example, if the scores were:

    8 65 89 86 55 91 64 89
    Your code should print 91 '''

#   My solution
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
score_max = 0
for score in student_scores:
    if score > score_max:
        score_max = score
print(f'Highest score: {score_max}')

#   Teachers solution
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#DAY5: LESSON 3 - For Loops with Range
''' The combination of the range() function with the Python For Loop allows us to run
    a loop for as many times as we wish. Instead of looping through each item in a List,
    we can loop through a range of numbers.
'''


#   range() - function
#   syntax: range(a,b,c) where a = start of range, b = end of range, c = how large steps per number in range.

range(1,10)
for number in range(1,10, 3):
    print(number)


#   GAUS CHALLENGE - calculate the sum of all numbers inside a range
#   My solution
number_list = list(range(1,101,1))
number_sum = 0
for number in number_list:
    number_sum = number_sum + number
print(number_sum)

#   Teachers solution
total = 0
for number in range(1, 101):
    total += number
print(total)

#DAY5: LESSON 3 - FizzBuzz Code challenge

#   My Solution
number_range = list(range(1,101,1))
for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
#   Teachers Solution
# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
  # First check if the number is divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 
  # Then check if the number is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
 
  # Finally check if the number is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
 
  # If it's not divisible by either of those numbers, just print the number
  else:
    print(number)


#DAY5: LESSON 4 - Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#   Easy Level - My solution
import random
easy_password = list()
slot = 0
while slot < nr_letters:
    easy_password.append(random.choice(letters))
    slot+= 1

slot = 0
while  slot < nr_symbols:
    easy_password.append(random.choice(symbols))
    slot += 1

slot = 0
while  slot < nr_numbers:
    easy_password.append(random.choice(numbers))
    slot += 1
print(f"Easy pw: {easy_password}")
print("".join(easy_password))

# Easy level - --> Teachers solution
'''
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
'''

#   Hard level - My solution
# Imports
import random

# Variables
hard_password = list()
char_type = ["letters", "numbers", "symbols"]
char_type_sel = ""

# Total user requested length of password
pw_length = nr_letters + nr_numbers + nr_symbols

# Loop Counters
pw_length_used = 0
letters_used = 0
symbols_used = 0
numbers_used = 0

# Loop iterating through and randomizing char type until pw length achieved
while pw_length_used <= pw_length:
        char_type_sel = random.choice(char_type)
        if char_type_sel == "letters" and letters_used < nr_letters:
            hard_password.append(random.choice(letters))
            letters_used += 1
        if char_type_sel == "symbols" and symbols_used < nr_symbols:
            hard_password.append(random.choice(symbols))
            symbols_used += 1
        if char_type_sel == "numbers" and numbers_used < nr_numbers:
            hard_password.append(random.choice(numbers))
            numbers_used += 1
        pw_length_used += 1
print(f"hard password: {hard_password}")
print("".join(hard_password))

#   Hard level --> Teachers solution
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
