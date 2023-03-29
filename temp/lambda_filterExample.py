# Let’s filter a list of numbers selecting only the numbers greater than 10 and return a list sorted in ascending order:
lst = [33, 3, 22, 2, 11, 1]
print(sorted(filter(lambda x: x > 10, lst)))
