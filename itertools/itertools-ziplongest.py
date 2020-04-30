from itertools import zip_longest


short_zip = zip('abcd', '123')
for z in short_zip:
    print(z)  # * Prints ('a',1) ('b',2) ('c',3)

long_zip = zip_longest('abcd', '123', fillvalue=None)
for z in long_zip:
    print(z)  # * Prints ('a',1) ('b',2) ('c',3) ('d',None)
