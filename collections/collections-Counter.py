from collections import Counter

c = Counter(["foo", "foo", "bar"])

print(c["foo"])  # 2
print(c["bar"])  # 1
print(c["baz"])  # 0

print(list(c.items()))  # [('foo',2),('bar',1)]
c["baz"] = 0
print(
    list(c.items())
)  # [('foo',2),('bar',1),('baz',0)] # * Note that baz is now in items
del c["baz"]

print(
    list(c.items())
)  # [('foo',2),('bar',1),('baz',0)] # * Use del to remove items completely, setting to 0 retains item

print(c.most_common(1))  # [('foo',2)]
print(c.most_common(2))  # [('foo',2),('bar',1)]

c["foo"] += 5
c["baz"] -= 3
print(list(c.items()))  # [('foo',7),('bar',1),('baz',-3)]

d = Counter(["foo", "foo", "baz", "quux"])
c.subtract(d)
print(list(c.items()))  # [('foo', 5), ('bar', 1), ('baz', -4), ('quux', -1)]
c2 = Counter({k: c[k] for k in c.keys()})
c2.subtract(c)
print(
    list(c2.items())
)  # [('foo', 0), ('bar', 0), ('baz', 0), ('quux', 0)] # * Of course negative subtraction is possible, hence quux is now 0

# ! Intersection
print(
    (c & d)["foo"]
)  # 2 # * d has only 2 entries of foo, hence this is the intersection

# ! Union
print((c | d)["foo"])  # 5 # * c has 5 entries of foo, this is the union


# Easily count the occurences of a character in a string.

s = "After the postoperative check at the clinic, Molly took him to the Tank War, mouth touched with hot gold as a gliding cursor struck sparks from the wall between the bookcases, its distorted face sagging to the bare concrete floor. Sexless and inhumanly patient, his primary gratification seemed to he in his jacket pocket. They floated in the shade beneath a bridge or overpass. Light from a service hatch at the rear wall dulling the roar of the console in faded pinks and yellows. The two surviving Founders of Zion were old men, old with the movement of the train, their high heels like polished hooves against the gray metal of the previous century. The tug Marcus Garvey, a steel drum nine meters long and two in diameter, creaked and shuddered as Maelcum punched for a California gambling cartel, then as a paid killer in the center of his closed left eyelid. A narrow wedge of light from a half-open service hatch at the rear of the arcade showed him broken lengths of damp chipboard and the dripping chassis of a gutted game console. Case had never seen him wear the same suit twice, although his wardrobe seemed to consist entirely of meticulous reconstruction’s of garments of the Villa bespeak a turning in, a denial of the bright void beyond the hull."

count_s = Counter(s)
print(
    count_s
)  # Counter({' ': 221, 'e': 132, 't': 86, 'a': 80, 'o': 75, 'i': 69, 'h': 67, 'r': 64, 's': 58, 'n': 58, 'l': 47, 'd': 44, 'c': 36, 'g': 28, 'f': 26, 'm': 25, 'u': 24, 'p': 18, 'w': 15, 'k': 14, 'v': 12, 'b': 12, ',': 11, 'y': 11, '.': 8, 'T': 4, 'M': 3, 'A': 2, 'C': 2, 'W': 1, 'S': 1, 'x': 1, 'j': 1, 'L': 1, 'F': 1, 'Z': 1, 'G': 1, '-': 1, '’': 1, 'V': 1})
