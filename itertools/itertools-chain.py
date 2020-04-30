from itertools import chain

letter_chain = chain(
    "ABC", "DE", "FGHIJKL", "MNOPQRSTU", "VW", "X", "YZ"
)  # Turn several iterables into one
for l in letter_chain:
    print(l)  # * Prints the letters of the alphabet

letter_chain_2 = chain.from_iterable(
    ["ABC", "DE", "FGHIJKL", "MNOPQRSTU", "VW", "X", "YZ"]
)  # Same as above but takes one iterable argument
