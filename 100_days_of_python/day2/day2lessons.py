#DAY2: LESSON 1 - Datatypes
	#1. STRINGS

	# SUBSCRIPTING
	# Subscripting = When you extract a positional character from a string
	# print("Hello""[x]) # returns the character in string position where x defines which numbered position. first character position is 0
	print("Hello"[4])

# --> 	# TIP - SUBSCRIPTING SUPPORT NEGATIVE POSITION EG -2 Note; starts from position 0
	print("Hello"[-4])

	#String - numbers treated as strings not numbers
	print("123" + "345") # returns 12345

	#2.INTEGERS = WHOLE NUMBER
	print (123+345) # Returns the numeric sum

# -->	# LARGE INTEGERS - Readability eg _can be used instead of 123,456,789 for large integer numbers.
	print(123_456_789)

	#3.FLOAT = Floating Point Number eg. Decimals  3141.59
	print(3.14159)

	#4.BOOLEAN - True/False note: capital T and F are important
	print(True)
	print(False)

#DAY2: LESSON 2 - Type Error, Checking and Conversion
	# len(12345) # Does not work because len() function does not support integer data type
	len("12345") # is the pause mini test answer

	# Each function expects to work with a certain set of datatypes

	#TYPE CHECKING
	# type() # Function checks which data type an object or variable etc. is
	# Takes 1-3 arguments
	print(type("Hello"))    # Returns <class 'str'>
	print(type(123))        # Returns <class 'int'>
	print(type(123.6))      # Returns <class 'float'>
	print(type(False))      # Returns <class 'bool'>

	# TYPE CONVERSION FUNCTIONS / TYPE CASTING
	# int()     - Casts to integer
	# float()   - Casts to float
	# str()     - Casts to string
	# bool()    - Casts to boolean


	# All datatypes cannot be converted into other datatypes
	# e.g. a string datatype lett eg "A" cannot be converted into an int



	# Pause Challenge 3
	# Make this line of code run without errors:
	# print("Number of letters in your name: " + len(input("Enter your name")))
	print("Number of letters in your name: " + str(len(input("Enter your name"))))	# My solution

	# Teacher solution
	name_of_the_user = input("Enter your name")
	length_of_name = len(name_of_the_user)

	print(type("Number of letters in your name: "))  # str
	print(type(length_of_name))  # int

	print("Number of letters in your name: " + str(length_of_name))


