
# ! Combinatorial


from itertools import product, permutations, combinations, combinations_with_replacement, chain

# ! Default repeat is 1 meaning that each iterable is sampled just once, can sample multiple times
cards = product(chain(['A', 'J', 'Q', 'K'], range(1, 11)), [
                'Clubs', 'Spades', 'Hearts', 'Diamonds'])
for rank, suit in cards:
    print(f'{rank} of {suit}')

cards2 = product(['A', 'J'], ['Diamond', 'Spade'], repeat=2)
for p in cards2:
    print(p)  # * This blows up pretty quickly to 16 options

card_set = permutations(
    ['Ace of Hearts', 'Queen of Clubs', 'Two of Diamonds'], 3)
for p in card_set:
    print(p)  # * There are 6 ways to permute all three items

card_set2 = combinations(
    ['Ace of Hearts', 'Queen of Clubs', 'Two of Diamonds'], 2)
for p in card_set2:
    print(p)  # * There are 3 ways to pick 2 of the three

card_set3 = combinations_with_replacement(
    ['Ace of Hearts', 'Queen of Clubs', 'Two of Diamonds'], 2)
for p in card_set3:
    # * There are 6 ways to pick 2 of the three if the same card can be picked twice; i.e. it is replaced.
    print(p)
