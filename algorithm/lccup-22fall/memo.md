1. don't know generate `graph = [[] for _ in range(1000)]`

2. `indeg = outdeg = [0] * 1000` will cause `indeg` and `outdeg` point to the same pointer!

3. `collections.defaultdict(set)` `collections.defaultdict(list)`

```python
>>> import collections
>>> c = collections.defaultdict(set)
>>> c
defaultdict(<class 'set'>, {})
>>> c[1].add(2)
>>> c
defaultdict(<class 'set'>, {1: {2}})
```

```python
>>> li = collections.defaultdict(list)
>>> li
defaultdict(<class 'list'>, {})
>>> li[1].add(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
>>> li[1].append(2)
>>> li
defaultdict(<class 'list'>, {1: [2]})
```
