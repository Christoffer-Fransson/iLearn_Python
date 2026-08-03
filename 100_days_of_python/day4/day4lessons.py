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



