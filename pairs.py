
import os
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def pairs(k, arr):
    # Write your code here
    arr = set(arr)
    count = 0
    for i in arr:
        if i + k in arr:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
#
# Example
#
# There are three values that differ by : , , and . Return
#
# .
#
# Function Description
#
# Complete the pairs function below.
#
# pairs has the following parameter(s):
#
#     int k: an integer, the target difference
#     int arr[n]: an array of integers
#
# Returns
#
#     int: the number of pairs that satisfy the criterion
#
# Input Format
#
# The first line contains two space-separated integers
# and , the size of and the target value.
# The second line contains space-separated integers of the array
#
# .
#
# Constraints
#
# each integer
#
#     will be unique
#
# Sample Input
#
# STDIN       Function
# -----       --------
# 5 2         arr[] size n = 5, k =2
# 1 5 3 4 2   arr = [1, 5, 3, 4, 2]
#
# Sample Output
#
# 3
#
# Explanation
#
# There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. .