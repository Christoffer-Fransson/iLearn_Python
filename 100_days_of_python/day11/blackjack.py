#DAY11: Blackjack capstone project
from operator import truediv

import art
import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
player_hand = []

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
    else:
        print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"Computers final hand: {sum(computer_hand)}")
        print("You went over. You loose 😢")

        return False



run = True
while run:
    run_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
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
                check_bust(player_hand, hand_type="player")
                print(f"Your Cards: {player_hand}, current score {sum(player_hand)}")
            if choice.lower() == "n":
                print("temp:stands")

        print(f'Your Cards: {player_hand}, current score: {sum(player_hand)}')
        print(f"Computer's first card: {computer_hand[0]}")

    if run_choice.lower() == "n":
        run = False



#
#     # Type 'y' to get another cards, type 'n' to pass:
# -->     player_hand= (deal_hand(2,"player")")
#     print(f'Your cards: {player_hand}, current score: {sum(player_hand)}")
#     while len(player_hand) <2 and len(dealer_hand) <2:
#         print("dealer deals card to player")
#         player_hand.append(draw_card())
#
#         print("dealer deals card to dealer")
#         dealer_hand.append(draw_card())
#
#         print(f'Dealer hand: {dealer_hand}')
#         print(f'Player hand: {player_hand}')
#     choice = input("write 'hit' to to take a new card or 'stay' to not get more cards: ")
#     if choice.lower() == "hit":
#         player_hand.append(draw_card())
#         print(f'Dealer hand: {dealer_hand}')
#         print(f'Player hand: {player_hand}')
#         print(f"player hand sum = {sum(player_hand)}")
#
#     if choice.lower() == "stay":
#         print("Player stays")
#     if choice.lower() == "q":
#         bust = True
