from itertools as tee


def abc_gen():
    yield 'a'
    yield 'b'
    yield 'c'


g = abc_gen()

# ! a , b and c are separate iterators, do not attempt to advance g
a, b, c = tee(g, 3)
for l in a:
    print(l)  # * A is now exhausted

for l in a:
    print(l)  # * Prints nothing

for l in b:
    print(l)  # * But b is independent of a

for l in c:
    print(l)  # * And c is independent of b

# next(g) # ! This would raise a StopIteration exception
