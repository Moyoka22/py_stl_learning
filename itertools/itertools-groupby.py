from itertools import groupby

bands_by_first_letter_naive = groupby(
    ['ABBA', 'ACDC', 'Daft Punk', 'Black Eyed Peas', 'Gorillaz', 'Queen', 'Big Brovaz'], lambda x: x[0])
for key, group in bands_by_first_letter_naive:
    # Group is a itertools._grouper objeect
    print(f'Key: {key} ; Group: {list(group)}')
    """ When the grouper advances the Black Eyed Peas and Big Brovaz will be placed in separate groups but ABBA and ACDC which are concurrent are in the same group
     To handle this behaviour, sort the input first"""


bands_by_first_letter_properly = groupby(sorted(
    ['ABBA', 'ACDC', 'Daft Punk', 'Black Eyed Peas', 'Gorillaz', 'Queen', 'Big Brovaz']), lambda x: x[0])
for key, group in bands_by_first_letter_properly:
    # Group is a itertools._grouper objeect
    print(f'Key: {key} ; Group: {list(group)}')
