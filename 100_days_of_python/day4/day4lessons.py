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

#DAY4 - LESSON 2 - Lists
