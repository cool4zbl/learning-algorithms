# How to sort a dict by value

import operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1], reverse=True)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# Or
sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
