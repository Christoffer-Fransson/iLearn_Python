#DAY4 - LESSON 1 - Random module
# Video diving into psudorandom number generators
# --> https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs


import random
random_int = random.randint(1,10)
print(random_int)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

#   Head or tails challenge - My solution
coin_value = random.randint(0, 1)
print("Coin toss")
if coin_value == 0:
    print("Heads")
else:
    print("Tails")

#   Head or tails challenge - Teachers solution
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

#DAY4: LESSON 2 - Lists
#   Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
#   You can create a simple collection of ordered items using a Python list. e.g.

fruits = ["Cherry", "Apple", "Pear"]
#   Access items lin lists by square brackets and index position (0 is the first position)
print(fruits[1])

#   Negative indice -> counting backward still starting from position 0
print(fruits[-1])

#   Appending a list -> Adds information to the end of the list using append() function
fruits.append("Orange")

#   Editing an already registered position
fruits[1] = "Mandarin"
print(fruits[1])


#DAY4: LESSON 3 - Code challenge
#DAY4: LESSON 3 - Code Challenge -> Print a random name from a list
#   My solution
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
list_length = (len(friends)  -1)     # -1 since first position == position 0!
random_list_pos = random.randint(0,list_length)         # assigns a variable integer between 0 and list max length

print(friends[random_list_pos])

#   Teachers solution
#   Solution 1 - Using random.choise() function
import random
print(random.choice(friends))

#   Solution 2 - Using random.randint
random_index = random.randint(0,4)
print(friends[random_index])

#DAY4: LESSON 4 - IndexError and Nested lists
#   IndexError - is when you refer to list position out of range.
#   E.g. len(list) = 50 but since positing start at 0
#   you need to add -1 e.g. list_pos_max = len(list) - 1
#   otherwise you can call a position tha tdoes not exist resulting in Index Error

#   Nested lists - A list inside a list or "2d list"
twodimensional_list = [[1,2,3,4],[5,6,7,8]]
print(len(twodimensional_list))
print(f'list length: {len(twodimensional_list)}')
print(twodimensional_list)
print(f"position 0: {twodimensional_list[0]}")
print(f"position 1: {twodimensional_list[1]}")

# Nested position targeting
letters = ["a", "b", "c"]
numbers = ["1", "2", "3"]

two_dimensional = [letters, numbers]

print(two_dimensional[1][1])    # targets two_dimensional list position 1, then that list position 1


