# ! Shortest input sequence


import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)
from itertools import accumulate, chain, compress, dropwhile, takewhile

res1 = accumulate("ABCD")  # Default behaviour is to sum the iterable
for r in res1:
    logging.info(r)  # * Prints 'A', 'AB' , 'ABC' , 'ABCD'

fact = accumulate([1, 2, 3, 4, 5], lambda x, y: x * y)  # ! Can also use operator.mul
for f in fact:
    logging.info(f)  # * Prints 1 , 2 , 6 , 24 , 120

letter_chain = chain(
    "ABC", "DE", "FGHIJKL", "MNOPQRSTU", "VW", "X", "YZ"
)  # Turn several iterables into one
for l in letter_chain:
    logging.info(l)  # * Prints the letters of the alphabet

letter_chain_2 = chain.from_iterable(
    ["ABC", "DE", "FGHIJKL", "MNOPQRSTU", "VW", "X", "YZ"]
)  # Same as above but takes one iterable argument

selected_toppings = compress(
    ["Tomato", "Cheese", "Onions", "Ham", "Jalapenos"], [True, False, 1, 0, "Yes"]
)
for topping in selected_toppings:
    logging.info(topping)  # * Prints Tomato, Onions, Jalapenos

after_d = dropwhile(
    lambda x: x[0] == "D",
    ["Alpha", "Beta", "Charlie", "Delta", "Echo", "Foxtrot", "Alpha", "Beta"],
)
for a in after_d:
    logging.info(a)  # * Prints Delta, Echo, Foxtrot, Alpha, 'Beta'

before_d = takewhile(
    lambda x: x[0] != "D",
    ["Alpha", "Beta", "Charlie", "Delta", "Echo", "Foxtrot", "Alpha", "Beta"],
)

for a in before_d:
    logging.info(a)  # * Prints Alpha, Beta, Charlie
