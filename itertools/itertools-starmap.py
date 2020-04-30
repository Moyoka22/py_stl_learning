from itertools import starmap

""" ! Star in starmap is a reference to the star operator in python which expands arguments; 
 hence, starmap maps a function onto prepared tuple pairs, starmap(f,args) -> map(f,arg) for arg in args"""

using_map = map(lambda x: x[0]**x[1], [(1, 2), (2, 3), (3, 4), (4, 5)])
for u in using_map:
    print(u)

using_starmap = starmap(pow, [(1, 2), (2, 3), (3, 4), (4, 5)])
for u in using_starmap:
    print(u)
