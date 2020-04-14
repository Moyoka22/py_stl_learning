from itertools import count, cycle, repeat


import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)

# ! Infinite iterators

c = count(0)  # A lazy, infinite counter
for i in c:
    if i > 10:
        break
    logging.info(i)  # * Prints 0...10

cy = cycle(
    ("pop", "six", "squish", "uh-uh", "cicero", "lipchitz")
)  # Takes an iterable object and returns
for i in range(0, 15):
    logging.info(next(cy))
else:
    logging.info("They had it coming!")

wakanda_forever = repeat("Wakanda")
for i in range(0, 15):
    logging.info(next(wakanda_forever))

wakanda_four_times = repeat("Wakanda...", 4)
for w in wakanda_four_times:
    logging.info(w)
