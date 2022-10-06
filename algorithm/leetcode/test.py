import collections
import numbers


def sol(a):
    string = ''
    for i in a:
        string += str(i)

    seen = {}
    for c in string:
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    print(seen)

    _, maxTimes = collections.Counter(string).most_common()[0]
    print(maxTimes)
    ans = []
    for k, v in seen.items():
        if v == maxTimes:
            ans.append(int(k))
    ans.sort()
    return ans


a = [25, 2, 3, 57, 38, 41]
print(sol(a))
