import re

card = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card = card[::-1]
print(card.index('A'))

matrix = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
matrix = matrix.split('\n')


def identify_poker_hand(hand):
    # Count occurrences of each card
    card_counts = {card: hand.count(card) for card in set(hand)}

    # Sort cards by count in descending order
    sorted_cards = sorted(card_counts, key=lambda x: card_counts[x], reverse=True)

    # Determine the type of poker hand
    if card_counts[sorted_cards[0]] == 5:
        # Five of a kind
        return 6
    elif card_counts[sorted_cards[0]] == 4 and card_counts[sorted_cards[1]] == 1:
        # Four of a kind
        return 5
    elif card_counts[sorted_cards[0]] == 3 and card_counts[sorted_cards[1]] == 2:
        # Full house
        return 4
    elif card_counts[sorted_cards[0]] == 3 and card_counts[sorted_cards[1]] == card_counts[sorted_cards[2]] == 1:
        # Three of a kind
        return 3
    elif card_counts[sorted_cards[0]] == card_counts[sorted_cards[1]] == 2 and card_counts[sorted_cards[2]] == 1:
        # Two pair
        return 2
    elif card_counts[sorted_cards[0]] == 2 and card_counts[sorted_cards[1]] == card_counts[sorted_cards[2]] == card_counts[sorted_cards[3]] == 1:
        # One pair
        return 1
    else:
        # High card
        return 0

score = 0

type = []
rank = len(matrix)

# Find Five of a kind
for row in matrix:
    # Use regular expression to find both parts
    match = re.match(r'(\w+) (\d+)', row)
    # print(match)
    hand = match.group(1)
    bid = match.group(2)
    if identify_poker_hand(hand) == 3:
      type.append([hand,bid])
      matrix.remove(row)

for row in type:
    for elem in row[0]:
        print(elem)


print(matrix)

    




