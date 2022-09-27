# Recursion

```python
def recursion(self, level, param1, param2, ...):
    # terminator
    if level > MAX_LEVEL:
        # process result
        return

    # process logic in current level
    process(level, data...)

    # drill down
    self.recursion(level + 1, new_param1, ...)

    # restore the current level status
```
