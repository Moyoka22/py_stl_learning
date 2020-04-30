from itertools import count

# ! Infinite iterators

c = count(0)  # A lazy, infinite counter
for i in c:
    if i > 10:
        break
    print(i)  # * Prints 0...10
