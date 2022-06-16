deck_of_card = input().split()
number_of_shuffle = int(input())
for shuffle in range(number_of_shuffle):
    final_deck = []
    middle_of_deck = len(deck_of_card) // 2
    left_part = deck_of_card[0:middle_of_deck]
    right_part = deck_of_card[middle_of_deck::]
    for index in range(len(left_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])
    deck_of_card = final_deck
print(deck_of_card)
