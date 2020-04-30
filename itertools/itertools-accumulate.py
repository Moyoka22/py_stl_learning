# ! Shortest input sequence
from itertools import accumulate

res1 = accumulate("ABCD")  # Default behaviour is to sum the iterable
for r in res1:
    print(r)  # * Prints 'A', 'AB' , 'ABC' , 'ABCD'

fact = accumulate([1, 2, 3, 4, 5], lambda x, y: x *
                  y)  # ! Can also use operator.mul
for f in fact:
    print(f)  # * Prints 1 , 2 , 6 , 24 , 120
