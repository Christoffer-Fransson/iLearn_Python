#DAY11: Blackjack capstone project
from operator import truediv

import art
import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    card_value = random.choice(card)
    return card_value

def deal_hand(amount_cards, hand_type):
    i = 0
    while i < amount_cards:
        if hand_type.lower() == "player":
            player_hand.append(draw_card())
        if hand_type.lower() == "computer":
            computer_hand.append(draw_card())
        i += 1
    return player_hand, computer_hand

def check_bust(hand, hand_type):
    if sum(hand) < 21:
        if hand_type.lower() == "player":
            print(f'    Your cards: {player_hand}, current score: {sum(player_hand)}')
        elif hand_type.lower() == "computer":
            print(f'    Computer cards: {computer_hand[0]}, current score: {sum(computer_hand)}')
        return True
    elif sum(hand) == 21:
        print("temp yay")
    else:           # if >21 returns false killing the loop
        return False

run = True

# Game start / Outer game loop
while run:
    computer_hand = []          # Sets/resets player hand to empty
    player_hand = []            # Sets/resets computer hand to empty
    run_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    # Inner game interactivity loop
    if run_choice.lower() == "y":
        print(art.logo)
        deal_hand(2,"player")
        deal_hand(2,"computer")
        print(f'Your cards: {player_hand}, current score: {sum(player_hand)}')
        print(f"Computer's first card: {computer_hand[0]}")

        keep_playing = True
        while keep_playing:
            choice = input("Type 'y' to get another card, type 'n' to pass  ")
            if choice.lower() == "y":
                deal_hand(1,"player")
                keep_playing = check_bust(player_hand, hand_type="player")              # checks hand sum and if stop loop criteria is met
                print(f"Your Cards: {player_hand}, current score {sum(player_hand)}")

            if choice.lower() == "n":
                print("temp:stands")

    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Computers final hand: {computer_hand}, final score:{sum(computer_hand)}")
    if sum(player_hand) > 21:
        print("You went over. You loose 😢")


 #       print(f'Your Cards: {player_hand}, current score: {sum(player_hand)}')
 #       print(f"Computer's first card: {computer_hand[0]}")

    if run_choice.lower() == "n":
        run = False

