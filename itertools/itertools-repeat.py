from itertools import repeat

wakanda_forever = repeat("Wakanda")

for i in range(0, 15):
    print((next(wakanda_forever)))

yeah_3x = repeat("Yeah", 3)
for yeah in yeah_3x:
    print(yeah)
