# import module
from random import choice as rc

# list of all card types
cards = [{'card': 'A', 'value': 11}, {'card': 2, 'value': 2}, {'card': 3, 'value': 3},
         {'card': 4, 'value': 4}, {'card': 5, 'value': 5}, {'card': 6, 'value': 6},
         {'card': 7, 'value': 7}, {'card': 8, 'value': 8}, {'card': 9, 'value': 9},
         {'card': 10, 'value': 10}, {'card': 'J', 'value': 10}, {'card': 'Q', 'value': 10},
         {'card': 'K', 'value': 10}]

# sum of card values (adjusted for aces being 1/11)
def hand_total(hand):
    total = 0
    aces = 0

    for card in hand:
        total += card['value']

        if card['card'] == 'A':
            aces += 1
        
    while total>21 and aces > 0:
            total -= 10 
            aces -=1

    return total 

# returns all cards in current hand as a joined string
def all_cards(current_hand):
    all_values = []

    for card in current_hand:
        all_values.append(str(card['card']))

    return ' '.join(all_values)

# player and dealer initial cards + totals
player_card_1 = rc(cards)
player_card_2 = rc(cards)
player_hand = [player_card_1, player_card_2]

dealer_card_1 = rc(cards)
dealer_card_2 = rc(cards)
dealer_hand = [dealer_card_1, dealer_card_2]

player_total = hand_total(player_hand)
dealer_total = hand_total(dealer_hand)

print(all_cards(player_hand))
print(f'Total = {player_total}')
print(f'Dealer\'s card: {dealer_card_1['card']}')

# game function
if player_total == 21:
    print('Blackjack! Player wins.')
else:
    decision = input('Would you like to hit or stand?')

    i = 3

    while decision == 'hit':
        player_card_i = rc(cards)
        player_hand.append(player_card_i)
        player_total = hand_total(player_hand)
        print(f'Current hand: {all_cards(player_hand)}')
        print(f'New total: {player_total}')
        i += 1
        if player_total > 21:
            print('Bust! Better luck next time')
            break
        decision = input('Would you like to hit or stand?')

    if player_total <= 21:

        print(f'Dealer\'s cards: {all_cards(dealer_hand)}')
        print(f'Dealer\'s current total: {dealer_total}')

        i = 3

        while dealer_total <= 16:
            dealer_card_i = rc(cards)
            dealer_hand.append(dealer_card_i)
            dealer_total = hand_total(dealer_hand)
            print(f'Dealer\'s current hand: {all_cards(dealer_hand)}')
            print(f'Dealer\'s current total: {dealer_total}')
            i += 1
        if dealer_total > 21:
            print('Dealer bust! Player wins')
        elif dealer_total > player_total:
            print('Dealer wins! Better luck next time')
        elif player_total > dealer_total:
            print('Player wins!')
        else:
            print('Push!')

