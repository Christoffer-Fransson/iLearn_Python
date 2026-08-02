#DAY3: Control Flow and Logical Operators

#DAY3: LESSON 1 - IF ELSE CONDITIONS
'''	 Example: IF statement
	water_level = 50
	if water_level >  80:
		print("Drain water")
	else: 
		print("Continue")




-->             An if statement can be visualised by a XOR gate. 
                Cross pollination with process development / charting
                
                +-----------+
                |   Start   |
                +-----------+
                      |
                      v
                 .-----------.
                /  Height >   \
                \   120cm?    /
                 '-----------'
             No /             \ Yes
               v               v
      +---------------+  +-------------+
      |   Can't ride   |  |  Can ride   |
      +---------------+  +-------------+
'''


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before youc an ride.")

   # COMPARISON OPERATORS
'''
    Operator    Meaning
    >           Greater than
    >           Less than
    >=          greather than or equal to
    <=          less than or equal to
    ==          equal to
    !=          not equal to
'''

#DAY3: LESSON 2 - Modulo operator %
'''
Modulo operator goes between two numbers and is a binary operator.
It works out what is the remainder after the division
e.g. 10 % 5 = 2   returns 0
because: 5 goes into 10 exactly two times with no remainder

10 % 3 = 3.33333333 returns 1 becuase it is a binary operator

CLAUDE'S EXPLANATION OF MODULO:
    Think of a clock
    An analog clock only has the numbers 1–12. If the clock shows 10 and you add 5 hours, it doesn't become "15" — it becomes 3, because it "wraps around" and starts over from 1.
    That's exactly what modulo does. 15 % 12 = 3 — same thing as the clock.

    Modulo answers the question: "where do I end up if I keep counting around a circle of a certain size?"

    Another picture: leftovers from splitting things up
    Imagine you have 10 candies and want to split them evenly between 3 people. Each person gets 3 candies (that's 10 // 3, integer division). But there's 1 candy left over that can't be split evenly — that's 10 % 3 = 1.
    So modulo is "what's left over when I divide things into equal-sized groups."
    Why it's actually used in practice

    1. Even/odd check
    Code example:
if n % 2 == 0:
    print("even number")
else:
    print("odd number")

    Every time you divide by 2, the remainder is either 0 or 1. That's enough to determine even/odd.

    2. "Wrap-around" in lists or loops
    If you have a list of 7 elements and want to loop around (index 8 should become index 1, index 9 should become index 2, and so on):

index = i % len(list)

    This is used a lot in games (e.g., rotating a player between multiple teams) and in circular buffers.

    3. Checking if a number divides evenly into another
n % 5 == 0 means n is divisible by 5 with no remainder — common for things like "every 5th row should have a different color" or FizzBuzz-type problems.

    4. Time calculations
    Converting seconds into minutes and seconds:

total_seconds = 130
minutes = total_seconds // 60   # 2
seconds = total_seconds % 60    # 10

    Here you see // and % working together — the integer part and the remainder, just like the clock example.
'''

# Even number modulo checker
number_to_check = int(input("What is the number you want to check? "))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

#DAY3: LESSON 3 - Nested if statements and elif statements
'''
                +-----------+
                |   Start   |
                +-----------+
                      |
                      v
                 .-----------.
                /  Height >   \
                \   120cm?    /
                 '-----------'
             No /             \ Yes
               v               v
      +---------------+  +-------------+
      |   Can't ride   |  |  Can ride   |
      +---------------+  +-------------+
                                |
                                v
                           .---------.
                          /    age    \
                          \           /
                           '---------'
              18 or under /           \ Over 18
                         v             v
                  +-----------+  +-----------+
                  |    $7     |  |   $12     |
                  +-----------+  +-----------+
'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

#   elif
'''
                      |
                      v
                +-----------+
                | Can ride  |
                +-----------+
                      |
                      v
                 .---------.
                /    age    \
                \           /
                 '---------'
     under 12   /     |     \   Over 18
               v       v      v
        +--------+ +--------+ +--------+
        |   $5   | |   $7   | |  $12   |
        +--------+ +--------+ +--------+
                      12-18

'''
#   Rollercoaster with elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

	# Code challenge
weight = 85
height = 1.85

bmi = weight / (height ** 2)

	# Do not modify the values above
	# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")
#DAY3: Lesson 4 - Multiple ifs
'''

                 .---------.
                /    age    \
                \           /
                 '---------'
     under 12   /     |     \   Over 18
               v       v      v
        +--------+ +--------+ +--------+
        |   $5   | |   $7   | |  $12   |
        +--------+ +--------+ +--------+
                      12-18
             \        |        /
              \       |       /
               v      v      v
                (merge point)
                      |
                      v
                 .-----------.
                /    want     \
                \   photos?   /
                 '-----------'
             No /             \ Yes
               v               v
        (straight down)   +--------+
               |           |   $3   |
               |           +--------+
                \             /
                 \           /
                  v         v
            +---------------------+
            | The total bill is $x|
            +---------------------+
'''

# 	Roller coast example with multiple ifs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for yes and n for No")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

#DAY3: LESSON 5 - Coding challenge
#	My solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill +=15
elif size =="M":
    bill +=20
elif size =="L":
    bill +=25
if pepperoni == "Y":
   if size == "S":
       bill +=2
   else:
       bill +=3
if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}.")

#DAY3: LESSON 6 - Logical Operators
#   and
#   or
#   not

#   and - logical operator works
#   True And True = true
#   True and False = False
#   False and True = False

#   or - logical operator works
#   if c or d were true = true
#   if c and d wer true = true
#   if c and d wer false = false

#   not - invertes e.g.
#   if true = false
#   if false = true

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

