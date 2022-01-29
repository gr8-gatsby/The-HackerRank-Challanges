# you should iterate the enumerated cost list and

def whatFlavors(cost, money):
    # Write your code here
    cost_dict = dict()
    for pos, price_1 in enumerate(cost, 1):
        price_2 = money - price_1
        if price_2 in cost_dict:
            print(cost_dict[price_2], pos)
            return
        else:
            cost_dict[price_1] = pos


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)


# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.
#
# Given the value of
# and the of each flavor for trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a
#
# . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.
#
# Example
#
#
# They would purchase flavor ID's and for a cost of . Use
#
# based indexing for your response.
#
# Note:
#
#     Two ice creams having unique IDs
#
# and may have the same cost (i.e.,
#
#     ).
#     There will always be a unique solution.
#
# Function Description
#
# Complete the function whatFlavors in the editor below.
#
# whatFlavors has the following parameter(s):
#
#     int cost[n] the prices for each flavor
#     int money: the amount of money they have to spend
#
# Prints
#
#     int int: the indices of the two flavors they will purchase as two space-separated integers on a line
#
# Input Format
#
# The first line contains an integer,
#
# , the number of trips to the ice cream parlor.
#
# Each of the next
# sets of
#
# lines is as follows:
#
#     The first line contains
#
# .
# The second line contains an integer,
# , the size of the array
# .
# The third line contains
# space-separated integers denoting the
#
#     .
#
# Constraints
#
# Sample Input
#
# STDIN       Function
# -----       --------
# 2           t = 2
# 4           money = 4
# 5           cost[] size n = 5
# 1 4 5 3 2   cost = [1, 4, 5, 3, 2]
# 4           money = 4
# 4           cost[] size n = 4
# 2 2 4 3     cost = [2, 2, 4, 3]