from collections import defaultdict

default_url = "http://127.0.0.1:5000"
d = defaultdict(lambda: default_url)

d["resource_four"] = "http://127.0.0.1:3000"

print(d["resource_one"])  # http://127.0.0.1:5000
print(d["resource_two"])  # http://127.0.0.1:5000
print(d["resource_three"])  # http://127.0.0.1:5000
print(d["resource_four"])  # http://127.0.0.1:3000

print(
    d.items()
)  # dict_items([('resource_four', 'http://127.0.0.1:3000'), ('resource_one', 'http://127.0.0.1:5000'),
# ('resource_two', 'http://127.0.0.1:5000'), ('resource_three', 'http://127.0.0.1:5000')])

d2 = defaultdict(
    list
)  # * The default factory will initialise the value for a key by calling the factory method

words = ["Abracada", "Amazing,", "Bananarama", "Cawabunga", "Disappearama"]

for w in words:
    d2[w[0]].append(w)

print(
    d2.items()
)  # dict_items([('A', ['Abracada', 'Amazing,']), ('B', ['Bananarama']), ('C', ['Cawabunga']), ('D', ['Disappearama'])])

# Above can also be done with groupby
from itertools import groupby

g = groupby(words, lambda x: x[0])
print(
    [(x[0], list(x[1])) for x in g]
)  # [('A', ['Abracada', 'Amazing,']), ('B', ['Bananarama']), ('C', ['Cawabunga']), ('D', ['Disappearama'])]
