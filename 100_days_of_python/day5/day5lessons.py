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
