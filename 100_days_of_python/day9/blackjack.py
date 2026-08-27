#DAY11: Dev Blackjack capstone file

#DAY11: Blackjack capstone project
import art
import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
print(art.logo)

def draw_card():
    card_value = random.choice(card)
    return card_value

def check_bust(player_hand, dealer_hand):
    if sum(player_hand) > 21:
        return True
    if sum(dealer_hand) > 21:
        return True

bust = False
while not bust:
    while len(player_hand) <2 and len(dealer_hand) <2:
        print("dealer deals card to player")
        player_hand.append(draw_card())

        print("dealer deals card to dealer")
        dealer_hand.append(draw_card())

        print(f'Dealer hand: {dealer_hand}')
        print(f'Player hand: {player_hand}')
    choice = input("write 'hit' to to take a new card or 'stay' to not get more cards: ")
    if choice.lower() == "hit":
        player_hand.append(draw_card())
        print(f'Dealer hand: {dealer_hand}')
        print(f'Player hand: {player_hand}')
        print(f"player hand sum = {sum(player_hand)}")

    if choice.lower() == "q":
        bust = True


