from functools import islice


from string import ascii_lowercase
# ! Not that it is [5,13) but the first index is 0
someletters = islice(ascii_lowercase, 5, 13)
for l in someletters:
    print(l)  # * Prints 'f g h i j k l m'
