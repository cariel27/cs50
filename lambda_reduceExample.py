from functools import reduce
# Operates on the first two items of an iterable and saves the result
# Operates on the saved result and the next item of the iterable
# Proceeds in this way over the pairs of values until all the items of
# the iterable are used
lst = [1, 2, 3, 4, 5]
reduce(lambda x, y: x + y, lst)
