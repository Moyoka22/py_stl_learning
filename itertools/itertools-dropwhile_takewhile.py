from itertools import dropwhile, takewhile

after_d = dropwhile(
    lambda x: x[0] == "D",
    ["Alpha", "Beta", "Charlie", "Delta", "Echo", "Foxtrot", "Alpha", "Beta"],
)
for a in after_d:
    print(a)  # * Prints Delta, Echo, Foxtrot, Alpha, 'Beta'

before_d = takewhile(
    lambda x: x[0] != "D",
    ["Alpha", "Beta", "Charlie", "Delta", "Echo", "Foxtrot", "Alpha", "Beta"],
)

for a in before_d:
    print(a)  # * Prints Alpha, Beta, Charlie
