# Write your code below this line 👇
# DAY 1: Lesson 1 - print() 
print("Hello world!")

# DAY 1: Lesson 2
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")


# Debugging session
# Fix the code below 👇
'''
print(Notes from Day 1")
 print("The print statement is used to output strings")
print("Strings are strings of characters"
priint("String Concatenation is done with the + sign")
print(("New lines can be created with a \ and the letter n")
'''

# Below code is fixed
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


# DAY 1: Lesson 3 - input()
# print("What is your name?")  	 # PRINTS ONLY
# input("What is your name?)	  # Prints and lets user inputs text

# Mini challenge
print("Hello" + input("What is your name?") + "!")

# DAY 1: LESSON 4 - VARIABLES
# DAY 1: Lesson 4 - minichallenge variables and len()
name = input("Enter your name: ")		# with variables
print(len(name))

print(len(input("Enter your name: ")))		# and as one single line

username = input("Enter your name: ")		# and with variable segmented solution
length = len(username)
print (length)

# CODE EXCERSIZE 3
glass1 = "milk"
glass2 = "juice"
glass3 = glass2
glass2 = glass1
glass1 = glass3

