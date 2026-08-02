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


