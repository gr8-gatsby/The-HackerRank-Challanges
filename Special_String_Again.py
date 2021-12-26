from collections import Counter
from itertools import groupby


def substrCount(n, s):
    res = 0
    i = 0

    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1

        res += count * (count + 1) // 2
        i += 1

    for i in range(1, n):
        count = 1
        while i + count < n and i - count >= 0 and s[i] != s[i - 1] and s[i - count] == s[i + count] and s[i - 1] == s[i - count]:
            count += 1

        res += count - 1

    return res


a = 'mnonopoo'
print(substrCount(8, a))

#
#
