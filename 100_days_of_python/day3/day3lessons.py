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

