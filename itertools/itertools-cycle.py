from itertools import cycle

cy = cycle(
    ("pop", "six", "squish", "uh-uh", "cicero", "lipchitz")
)  # Takes an iterable object and returns
for i in range(0, 15):
    print(next(cy))
else:
    print("They had it coming!")
