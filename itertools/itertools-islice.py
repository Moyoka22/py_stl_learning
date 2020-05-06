from itertools import islice

# islice = iterator slice

from string import ascii_lowercase

# ! Not that it is [5,13) but the first index is 0
some_letters = islice(ascii_lowercase, 5, 13)
for l in some_letters:
    print(l)  # * Prints 'f g h i j k l m'

# ! islice will automatically stop if the iterator is exhausted
some_more_letters = islice(ascii_lowercase, 0, 100, 10)  # * Can specify a step
for l in some_more_letters:
    print(l)  # * Prints 'a k u'
