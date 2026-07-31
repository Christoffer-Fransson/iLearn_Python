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


#DAY2: LESSSON 3 - Mathematical Operations
	print("My age: " + str(12))
	print(123 + 456)
	print(7 - 3)
	print (3 * 2)
	print (6 / 3)

	# IMPLICIT TYPECASTING
	# Note: Division operator / returns a float datatype
	# E.G. print(6 / 3) returns 2.0

	# print (6 // 3) returns integer datatype. BE CAREFUL USING THIS
	# What this does is do 6 / 3 and then remove all the decimals
	print(6 // 3)   # returns 2
	print(5 // 3)   # returns 1 (expecting 1.5) can be useful when you want return without decimal place

	# Exponent "to the power of"
	print(2 ** 2)     # (is 2 with an exponent of 2)
	print(2 ** 3)

	# TIP Careful with mathematical operations
	# Certain priorities of operation. eg PEMDAS

	# PEMDAS
	# Order of mathematical operations  print(123 + 456)
	print(7 - 3)
	print (3 * 2)
	print (6 / 3)

	# IMPLICIT TYPECASTING
	# Note: Division operator / returns a float datatype
	# E.G. print(6 / 3) returns 2.0

	# print (6 // 3) returns integer datatype. BE CAREFUL USING THIS
	# What this does is do 6 / 3 and then remove all the decimals
	print(6 // 3)   # returns 2
	print(5 // 3)   # returns 1 (expecting 1.5) can be useful when you want return without decimal place

	# Exponent "to the power of"
	print(2 ** 2)     # (is 2 with an exponent of 2)
	print(2 ** 3)

	# TIP Careful with mathematical operations
	# Certain priorities of operation. eg PEMDAS

	# PEMDAS
	# Order of mathematical operations (if same priority, priorities from left to right)
	# Parentheses, Exponents, Multiplications/Dvision, Addition/Subtraction
	# E.G (in order of priority)
	# 1. () - Parenthesis
	# 2. ** - Exponents
	# 3. * - Multiplication
	# 4. * or / - Multiplication / Division
	# 5. + or -  - Addition or subtraction
	
	print( 3 * 3 + 3 / 3 -3) # Returns 7.0
	# How to change the result to 3

