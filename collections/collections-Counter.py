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
