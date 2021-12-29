# this is the 'no fast enough' version
from collections import Counter

def substrCount(s):

    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(Counter(s[i:j+1])) == 1 or (len(Counter(s[i:j+1])) == 2 and len(s[i:j+1]) % 2 == 1 and s[(i+j) // 2] != s[i] and s[(i+j) // 2] != s[j]):
                count += 1

    return count




# A string is said to be a special string if either of two conditions is met:
# 
#     All of the characters are the same, e.g. aaa.
#     All characters except the middle one are the same, e.g. aadaa.
# 
# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
# 
# Example
# contains the following special substrings:
# 
# .
# 
# Function Description
# 
# Complete the substrCount function in the editor below.
# 
# substrCount has the following parameter(s):
# 
#     int n: the length of string s
#     string s: a string
# 
# Returns
# - int: the number of special substrings
# 
# Input Format
# 
# The first line contains an integer,
# , the length of .
# The second line contains the string
# 
# .
# 
# Constraints
# 
# 
# Each character of the string is a lowercase English letter,
# 
# .
# 
# Sample Input 0
# 
# 5
# asasd
# 
# Sample Output 0
# 
# 7 
# 
# Explanation 0
# 
# The special palindromic substrings of
# are
# 
# Sample Input 1
# 
# 7
# abcbaba
# 
# Sample Output 1
# 
# 10 
# 
# Explanation 1
# 
# The special palindromic substrings of
# are
# 
# Sample Input 2
# 
# 4
# aaaa
# 
# Sample Output 2
# 
# 10
# 
# Explanation 2
# 
# The special palindromic substrings of
# are 
