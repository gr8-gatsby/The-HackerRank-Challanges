# this is the 'no fast enough' version
from collections import Counter

def substrCount(s):

    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(Counter(s[i:j+1])) == 1 or (len(Counter(s[i:j+1])) == 2 and len(s[i:j+1]) % 2 == 1 and s[(i+j) // 2] != s[i] and s[(i+j) // 2] != s[j]):
                count += 1

    return count


a = 'mnonopoo'
print(substrCount(a))
