#DAY9: Dictionaries, Nested Lists + Dictionaries, Blind Acution project
#   Dictionaries Lesson 1

# Syntax
'''
{key: value}
e.g.
{"bug": "An error in a program that prevents the program from running as expected."}


# To add multiple key value pairs use comma , as separator
{
"bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again.",
}
'''
# How dictionaries are written in code often.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Key can also be integer
programming_dictionary[123] = "Numbers works as keys. remember they dont need "" when calling it."
print(programming_dictionary[123])

empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)   # prints the empied dictionary

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#DAY9: Nested lists and Dictionaries

'''     You can add lists or Dictionaries inside a dictionary as value
{
    Key: [List],
    Key2: {Dict},
}
'''

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
'''
travel_log = {
    "France": "Paris", "Lille", "Lyon", # This doesnt work needs to be turned into a list
}
'''
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],  # This works eg. using a list as value.
    "Germany": ["Stuttgart", "Berlin"],
}

# Challenge how to print Lille
print(travel_log['France'][1])

nested_list = ["A", "B", ["C", "D"]]    # Example of 2D-list eg a list in a list
print((nested_list[2])[1])              # Messy but it worked. :) ()-parenthes was unnecessary
print(nested_list[2][1])                # Teachers solution

# Nesting a dictionary within a dictionary
travel_log2 = {
    "France":{
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
# Challenge print Stuttgart from travel log
print(travel_log2["Germany"]["cities_visited"][2])      # Teachers solution


#DAY9: Blind Auction Project
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

import art
print(art.logo)
received_bids = {}
keep_running = True
bidder_list = []
bids = []

while keep_running == True:
    bidder_list.append(input("What is your name?:"))
    bids.append(int(input("What is your bid?:")))
    received_bids["Bidder"] = bidder_list
    received_bids["Bids"] = bids

    choice= input("Are there any other bidders? Type 'yes' or 'no'.")
    if choice == 'yes':
        print("\n" * 100)
        keep_running = True

    elif choice == 'no':
        keep_running = False
    else:
        keep_running = True
# TODO-4: Compare bids in dictionary     
winning_bid = max(received_bids["Bids"])
# for bid in received_bids["Bids"]:
#     if bid > winning_bid:
#         winning_bid = bid
winning_bid_position = received_bids["Bids"].index(winning_bid)
print(f'{received_bids["Bidder"][winning_bid_position]} bidding {received_bids["Bids"][winning_bid_position]} won the auction')

