#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import *

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    aa, bb, cc = 0, 0, 0

    count = 0

    while bb < len(b):
        while aa < len(a) and a[aa] <= b[bb]:
            aa += 1

        while cc < len(c) and c[cc] <= b[bb]:
            cc += 1

        count += aa * cc
        bb += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()


# Given arrays of different sizes, find the number of distinct triplets where is an element of , written as , , and , satisfying the criteria:
#
# .
#
# For example, given
# and , we find four distinct triplets:
#
# .
#
# Function Description
#
# Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.
#
# triplets has the following parameter(s):
#
#     a, b, c: three arrays of integers .
#
# Input Format
#
# The first line contains
# integers , the sizes of the three arrays.
# The next lines contain space-separated integers numbering
#
# respectively.
#
# Constraints
#
# Output Format
#
# Print an integer representing the number of distinct triplets.
#
# Sample Input 0
#
# 3 2 3
# 1 3 5
# 2 3
# 1 2 3
#
# Sample Output 0
#
# 8
#
# Explanation 0
#
# The special triplets are
#
# .
#
# Sample Input 1
#
# 3 3 3
# 1 4 5
# 2 3 3
# 1 2 3
#
# Sample Output 1
#
# 5
#
# Explanation 1
#
# The special triplets are
#
# Sample Input 2
#
# 4 3 4
# 1 3 5 7
# 5 7 9
# 7 9 11 13
#
# Sample Output 2
#
# 12
#
# Explanation 2
#
# The special triplets are
# . 