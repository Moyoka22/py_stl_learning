
# ! Shortest input sequence - 2


import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)
from itertools import filterfalse, groupby, islice, starmap, tee, zip_longest




multi_21 = filterfalse(lambda x : any([(x % 3) != 0,(x % 7) != 0]),range(0,100)) # ! Note that rather than removing elements WHERE the predicate is false filterfalse returns only elements FOR WHICH the predicate is false; i.e. filter FOR false
for i in multi_21:
    logging.info(i) # * Prints out multiples of 21

bands_by_first_letter_naive = groupby(['ABBA','ACDC','Daft Punk','Black Eyed Peas','Gorillaz','Queen','Big Brovaz'], lambda x : x[0])
for key, group in bands_by_first_letter_naive:
    logging.info(f'Key: {key} ; Group: {list(group)}') # Group is a itertools._grouper objeect
    """ When the grouper advances the Black Eyed Peas and Big Brovaz will be placed in separate groups but ABBA and ACDC which are concurrent are in the same group
     To handle this behaviour, sort the input first"""


bands_by_first_letter_properly = groupby(sorted(['ABBA','ACDC','Daft Punk','Black Eyed Peas','Gorillaz','Queen','Big Brovaz']), lambda x : x[0])
for key, group in bands_by_first_letter_properly:
    logging.info(f'Key: {key} ; Group: {list(group)}') # Group is a itertools._grouper objeect

from string import ascii_lowercase
someletters = islice(ascii_lowercase,5,13) # ! Not that it is [5,13) but the first index is 0
for l in someletters:
    logging.info(l) # * Prints 'f g h i j k l m'



""" ! Star in starmap is a reference to the star operator in python which expands arguments; 
 hence, starmap maps a function onto prepared tuple pairs, starmap(f,args) -> map(f,arg) for arg in args"""

using_map = map(lambda x: x[0]**x[1], [(1,2),(2,3),(3,4),(4,5)])
for u in using_map:
    logging.info(u)

using_starmap = starmap(pow,[(1,2),(2,3),(3,4),(4,5)])
for u in using_starmap:
    logging.info(u)

def abc_gen():
    yield 'a'
    yield 'b'
    yield 'c'

g  = abc_gen() 
a, b ,c = tee(g,3) # ! a , b and c are separate iterators, do not attempt to advance g
for l in a:
    logging.info(l) # * A is now exhausted 

for l in a:
    logging.info(l) # * Prints nothing

for l in b:
    logging.info(l) # * But b is independent of a 

for l in c:
    logging.info(l) # * And c is independent of b

# next(g) # ! This would raise a StopIteration exception

short_zip = zip('abcd','123')
for z in short_zip:
    logging.info(z) # * Prints ('a',1) ('b',2) ('c',3)

long_zip = zip_longest('abcd','123',fillvalue=None)
for z in long_zip:
    logging.info(z) # * Prints ('a',1) ('b',2) ('c',3) ('d',None)