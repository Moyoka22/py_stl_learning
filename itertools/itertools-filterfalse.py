


from itertools import filterfalse


# ! Note that rather than removing elements WHERE the predicate is false filterfalse returns
# ! only elements FOR WHICH the predicate is false; i.e. filter FOR false

multi_21 = filterfalse(lambda x: any(
    [(x % 3) != 0, (x % 7) != 0]), range(0, 100))
for i in multi_21:
    print(i)  # * Prints out multiples of 21
